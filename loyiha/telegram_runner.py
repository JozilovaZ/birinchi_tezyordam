"""Telegram bot yurituvchi - apps.py va management command ishlatadi."""
import time
import json
import sys
import threading
from urllib.request import urlopen, Request
from urllib.error import URLError

from django.conf import settings
from django.utils import timezone


def _default_log(m):
    print(m, flush=True)


def _default_err(m):
    print(m, file=sys.stderr, flush=True)


class TelegramBot:
    def __init__(self, log=None, err=None):
        self.token = settings.TELEGRAM_BOT_TOKEN
        self.base_url = f'https://api.telegram.org/bot{self.token}'
        self.offset = 0
        self.sent_reminders = set()
        self.log = log or _default_log
        self.err = err or _default_err

    def api_call(self, method, data=None, timeout=40):
        url = f'{self.base_url}/{method}'
        if data:
            req = Request(url, data=json.dumps(data).encode('utf-8'),
                          headers={'Content-Type': 'application/json'})
        else:
            req = Request(url)
        try:
            with urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            self.err(f"API xatolik: {e}")
            return None

    def get_updates(self):
        result = self.api_call('getUpdates', {'offset': self.offset, 'timeout': 25}, timeout=35)
        if result and result.get('ok'):
            updates = result.get('result', [])
            if updates:
                self.offset = updates[-1]['update_id'] + 1
            return updates
        time.sleep(1)
        return []

    def send_message(self, chat_id, text, parse_mode='HTML'):
        self.api_call('sendMessage', {
            'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode,
        })

    def process_update(self, update):
        message = update.get('message')
        if not message:
            return
        chat_id = message['chat']['id']
        text = message.get('text', '').strip()
        user = message.get('from', {})
        if text.startswith('/start'):
            parts = text.split(maxsplit=1)
            token = parts[1].strip() if len(parts) > 1 else ''
            self.cmd_start(chat_id, user, token)

    def cmd_start(self, chat_id, user, token=''):
        from loyiha.models import TelegramFoydalanuvchi, TelegramUlanishTokeni
        ism = user.get('first_name', '')
        username = user.get('username', '')
        tg_user, created = TelegramFoydalanuvchi.objects.get_or_create(
            telegram_id=chat_id,
            defaults={'ism': ism, 'username': username}
        )
        if not created:
            tg_user.ism = ism
            tg_user.username = username
            tg_user.faol = True
            tg_user.save()

        if token:
            try:
                t_obj = TelegramUlanishTokeni.objects.get(token=token)
                tg_user.foydalanuvchi = t_obj.foydalanuvchi
                tg_user.save()
                t_obj.delete()
                self.send_message(chat_id,
                    f"Assalomu alaykum, <b>{ism}</b>! ✅\n\n"
                    f"Akkountingiz <b>{t_obj.foydalanuvchi.username}</b> ga muvaffaqiyatli bog'landi.\n"
                    "Dori ichish vaqtingiz kelganda sizga xabar yuboraman."
                )
                return
            except TelegramUlanishTokeni.DoesNotExist:
                self.send_message(chat_id,
                    "⚠️ Ulanish kodi topilmadi yoki muddati tugagan.\n"
                    "Saytdan yangi havolani oling."
                )
                return

        if tg_user.foydalanuvchi_id:
            self.send_message(chat_id,
                f"Assalomu alaykum, <b>{ism}</b>!\n\n"
                "Dori ichish vaqtingiz kelganda sizga xabar yuboraman."
            )
        else:
            self.send_message(chat_id,
                f"Assalomu alaykum, <b>{ism}</b>!\n\n"
                "Eslatmalarni olish uchun saytga kiring va "
                "<b>Mening Dorixonam</b> sahifasidan Telegramni ulang."
            )

    def eslatma_loop(self):
        while True:
            try:
                self.eslatmalarni_tekshir()
            except Exception as e:
                self.err(f"Eslatma xatolik: {e}")
            time.sleep(60)

    def eslatmalarni_tekshir(self):
        from loyiha.models import Dori, TelegramFoydalanuvchi
        now = timezone.localtime()
        current_time = now.strftime('%H:%M')
        today_key = now.strftime('%Y-%m-%d')

        eslatmalar = Dori.objects.filter(
            eslatma_vaqti__isnull=False,
            foydalanuvchi__isnull=False,
        ).select_related('foydalanuvchi')

        for dori in eslatmalar:
            if not dori.eslatma_faol:
                continue
            dori_vaqt = dori.eslatma_vaqti.strftime('%H:%M')
            reminder_key = f"{today_key}_{dori.id}_{dori_vaqt}"
            if dori_vaqt != current_time or reminder_key in self.sent_reminders:
                continue

            tg_user = TelegramFoydalanuvchi.objects.filter(
                foydalanuvchi=dori.foydalanuvchi, faol=True
            ).first()
            if not tg_user:
                continue

            self.sent_reminders.add(reminder_key)
            qolgan = dori.eslatma_qolgan_kun
            text = (
                f"💊 <b>DORI ICHISH VAQTI</b> 💊\n"
                f"━━━━━━━━━━━━━━━━━━\n\n"
                f"🔔 Hurmatli foydalanuvchi,\n"
                f"dori ichish payti keldi!\n\n"
                f"📋 <b>Dori:</b> {dori.nomi}\n"
            )
            if dori.miqdor:
                text += f"💉 <b>Miqdor:</b> {dori.miqdor}\n"
            text += f"🕐 <b>Vaqt:</b> {dori_vaqt}\n"
            if dori.eslatma_tavsif:
                text += f"📝 <b>Izoh:</b> {dori.eslatma_tavsif}\n"
            if qolgan is not None:
                text += f"📅 <b>Eslatma:</b> yana {qolgan} kun\n"
            text += (
                f"\n━━━━━━━━━━━━━━━━━━\n"
                f"❤️ Sog'lig'ingiz — eng qimmatli boyligingiz!"
            )
            self.send_message(tg_user.telegram_id, text)
            self.log(f"Eslatma yuborildi: {dori.nomi} -> {tg_user.ism} ({dori_vaqt})")

        old_keys = {k for k in self.sent_reminders if not k.startswith(today_key)}
        self.sent_reminders -= old_keys

    def run(self):
        if not self.token:
            self.err("TELEGRAM_BOT_TOKEN sozlanmagan!")
            return
        self.log("Telegram bot ishga tushdi!")
        reminder_thread = threading.Thread(target=self.eslatma_loop, daemon=True)
        reminder_thread.start()
        while True:
            try:
                updates = self.get_updates()
                for update in updates:
                    self.process_update(update)
            except Exception as e:
                self.err(f"Xatolik: {e}")
                time.sleep(5)


_bot_started = False
_lock = threading.Lock()


def start_bot_in_background():
    """Django ishga tushganda botni daemon thread sifatida ishga tushirish."""
    global _bot_started
    with _lock:
        if _bot_started:
            return
        _bot_started = True

    def _runner():
        bot = TelegramBot()
        try:
            bot.run()
        except Exception as e:
            print(f"[Telegram bot fatal] {e}", file=sys.stderr)

    t = threading.Thread(target=_runner, daemon=True, name='telegram-bot')
    t.start()
