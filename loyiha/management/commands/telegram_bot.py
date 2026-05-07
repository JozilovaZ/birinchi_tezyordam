"""
Telegram bot - dori eslatmalari uchun.

Bot sayt (runserver) ishga tushganda avtomatik ishlaydi.
Alohida ishga tushirish uchun: python manage.py telegram_bot
"""
from django.core.management.base import BaseCommand

from loyiha.telegram_runner import TelegramBot


class Command(BaseCommand):
    help = "Telegram botni ishga tushirish (dori eslatmalari uchun)"

    def handle(self, *args, **options):
        bot = TelegramBot(
            log=lambda m: self.stdout.write(self.style.SUCCESS(m)),
            err=lambda m: self.stderr.write(self.style.ERROR(m)),
        )
        try:
            bot.run()
        except KeyboardInterrupt:
            self.stdout.write("\nBot to'xtatildi.")
