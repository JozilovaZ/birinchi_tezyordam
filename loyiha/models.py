from django.conf import settings
from django.db import models


class SaytSozlamalari(models.Model):
    # Umumiy
    sayt_nomi = models.CharField(max_length=200, default="FirstAid.uz", verbose_name="Sayt nomi")
    logo_matn = models.CharField(max_length=50, default="+", verbose_name="Logo belgisi")
    footer_matn = models.CharField(max_length=500, default="Birinchi Tez Yordam — Favqulodda vaziyatlarda professional tibbiy yordam ko'rsatish platformasi", verbose_name="Footer matni")

    # Bosh sahifa - Hero
    hero_sarlavha = models.CharField(max_length=500, default="Hayotni saqlab qolishga tayyormisiz?", verbose_name="Hero sarlavha")
    hero_tavsif = models.TextField(default="Birinchi Tez Yordam — bu favqulodda vaziyatlarda professional birinchi yordam ko'rsatish bo'yicha siz bilishingiz kerak bo'lgan barchani o'rgatadigan platforma. Har bir soniya muhim.", verbose_name="Hero tavsif")
    hero_rasm = models.ImageField(upload_to='sayt/', verbose_name="Hero rasm", blank=True, null=True)
    hero_rasm_url = models.URLField(default="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=700&q=80", verbose_name="Hero rasm URL (agar rasm yuklanmasa)", blank=True)
    hero_tugma1_matn = models.CharField(max_length=100, default="Video qo'llanmalar", verbose_name="Hero tugma 1 matni")
    hero_tugma2_matn = models.CharField(max_length=100, default="Katalogga o'tish", verbose_name="Hero tugma 2 matni")
    hero_stat_sarlavha = models.CharField(max_length=200, default="Haqiq pandemiya", verbose_name="Hero stat karta sarlavhasi")
    hero_stat_tavsif = models.CharField(max_length=200, default="protokol tayyor", verbose_name="Hero stat karta tavsifi")

    # Bosh sahifa - Qizil divider
    divider_1_raqam = models.CharField(max_length=10, default="01", verbose_name="Divider 1 raqam")
    divider_1_matn = models.CharField(max_length=200, default="Tez yordam protokollari", verbose_name="Divider 1 matn")
    divider_2_raqam = models.CharField(max_length=10, default="02", verbose_name="Divider 2 raqam")
    divider_2_matn = models.CharField(max_length=200, default="Interaktiv testlar", verbose_name="Divider 2 matn")
    divider_3_raqam = models.CharField(max_length=10, default="03", verbose_name="Divider 3 raqam")
    divider_3_matn = models.CharField(max_length=200, default="Shoshilinch raqamlar", verbose_name="Divider 3 matn")

    # Bosh sahifa - Kategoriyalar
    kategoriya_badge = models.CharField(max_length=100, default="Asosiy bilimlar", verbose_name="Kategoriya badge")
    kategoriya_sarlavha = models.CharField(max_length=200, default="Favqulodda holatlar", verbose_name="Kategoriya sarlavha")

    # Bosh sahifa - Xarita
    xarita_badge = models.CharField(max_length=100, default="Geolokatsiya", verbose_name="Xarita badge")
    xarita_sarlavha = models.CharField(max_length=200, default="Yaqin atrafdagi shifoxonalar", verbose_name="Xarita sarlavha")
    xarita_tavsif = models.TextField(default="Joylashuvingiz asosida eng yaqin tibbiy muassasalarni toping.", verbose_name="Xarita tavsif")

    # Bosh sahifa - Promo
    promo_badge = models.CharField(max_length=100, default="Bilim sinovi", verbose_name="Promo badge")
    promo_sarlavha = models.CharField(max_length=200, default="Bilimingizni sinab ko'ring!", verbose_name="Promo sarlavha")
    promo_tavsif = models.TextField(default="Birinchi yordam bo'yicha testni yechib, o'z bilimingizni baholang", verbose_name="Promo tavsif")
    promo_tugma_matn = models.CharField(max_length=100, default="Testni boshlash", verbose_name="Promo tugma matni")
    promo_stat1_raqam = models.CharField(max_length=20, default="10", verbose_name="Promo stat 1 raqam")
    promo_stat1_label = models.CharField(max_length=50, default="Savollar", verbose_name="Promo stat 1 label")
    promo_stat2_raqam = models.CharField(max_length=20, default="350", verbose_name="Promo stat 2 raqam")
    promo_stat2_label = models.CharField(max_length=50, default="Max ball", verbose_name="Promo stat 2 label")

    # Katalog sahifasi
    katalog_badge = models.CharField(max_length=100, default="Asosiy qo'llanma", verbose_name="Katalog badge")
    katalog_sarlavha = models.CharField(max_length=300, default="Birinchi tibbiy yordam bo'yicha bilimlar", verbose_name="Katalog sarlavha")
    katalog_tavsif = models.TextField(default="Har bir soniya muhim! Favqulodda vaziyatlarda to'g'ri harakat qilishni o'rganing va yaqinlaringizni himoya qiling.", verbose_name="Katalog tavsif")
    katalog_rasm = models.ImageField(upload_to='sayt/', verbose_name="Katalog banner rasmi", blank=True, null=True)
    katalog_protokol_sarlavha = models.CharField(max_length=200, default="Shoshilinch tibbiy protokollar", verbose_name="Protokol bo'lim sarlavhasi")
    katalog_protokol_tavsif = models.CharField(max_length=300, default="Favqulodda tibbiy holatlar uchun bosqichma-bosqich ko'rsatmalar", verbose_name="Protokol bo'lim tavsifi")

    # Shoshilinch sahifa
    shoshilinch_sarlavha = models.CharField(max_length=200, default="SHOSHILINCH YORDAM", verbose_name="Shoshilinch sarlavha")
    shoshilinch_tavsif = models.CharField(max_length=300, default="Xotirjam bo'ling! Quyidagi qadamlarni bajaring:", verbose_name="Shoshilinch tavsif")

    # Video sahifasi
    video_sarlavha = models.CharField(max_length=200, default="Video Qo'llanmalar", verbose_name="Video sahifa sarlavhasi")
    video_tavsif = models.TextField(default="Vizual qo'llanmalar orqali birinchi yordam ko'rsatishni o'rganing. Professional shifokorlar tomonidan tayyorlangan video darsliklar.", verbose_name="Video sahifa tavsifi")

    # Bolalar sahifasi
    bolalar_sarlavha = models.CharField(max_length=200, default="Bolalar bo'limi", verbose_name="Bolalar sahifa sarlavhasi")
    bolalar_tavsif = models.TextField(default="Bolalar uchun maxsus tayyorlangan birinchi yordam qo'llanmalari. Oddiy tilda, rasmlar bilan tushuntirilgan.", verbose_name="Bolalar sahifa tavsifi")
    bolalar_maslahat = models.TextField(default="Bolaga birinchi yordam ko'rsatishda tinchlikni saqlang. Bolalar kattalar kayfiyatini sezadi - sizning xotirjamligingiz bolaga ham o'tadi.", verbose_name="Bolalar maslahat matni")
    bolalar_cta_sarlavha = models.CharField(max_length=200, default="O'z qo'lingizda yengil tushuntiring!", verbose_name="Bolalar CTA sarlavha")
    bolalar_cta_tavsif = models.TextField(default="Bolangizga birinchi yordam haqida o'yinlar va rasmlar orqali o'rgating. Bilim hayot saqlab qoladi.", verbose_name="Bolalar CTA tavsif")

    # Dorilar sahifasi
    dorilar_sarlavha = models.CharField(max_length=200, default="Mening Dorixonam", verbose_name="Dorilar sahifa sarlavhasi")
    dorilar_tavsif = models.CharField(max_length=300, default="Sizning shaxsiy tibbiy inventaringiz va eslatmalaringiz.", verbose_name="Dorilar sahifa tavsifi")
    dorilar_maslahat = models.TextField(default="Dorilarni quruq, salqin va quyosh nuri tushadigan joydan uzoqda saqlang. Bolalar va 5 yoshgacha bolalar qo'li yetmaydigan joylarda saqlang.", verbose_name="Dorilar maslahat matni")

    # ============ NAVIGATSIYA VA FOOTER ============
    nav_home = models.CharField(max_length=50, default="Bosh sahifa", verbose_name="Nav: Bosh sahifa")
    nav_catalog = models.CharField(max_length=50, default="Katalog", verbose_name="Nav: Katalog")
    nav_quiz = models.CharField(max_length=50, default="Test", verbose_name="Nav: Test")
    nav_emergency = models.CharField(max_length=50, default="SHOSHILINCH", verbose_name="Nav: Shoshilinch tugma")
    footer_havola1 = models.CharField(max_length=100, default="Maxfiylik siyosati", verbose_name="Footer havola 1")
    footer_havola2 = models.CharField(max_length=100, default="Foydalanish shartlari", verbose_name="Footer havola 2")
    footer_havola3 = models.CharField(max_length=100, default="Tibbiy ogohlantirish", verbose_name="Footer havola 3")
    footer_havola4 = models.CharField(max_length=100, default="Sertifikatlangan yordam", verbose_name="Footer havola 4")

    # ============ UMUMIY UI MATNLARI ============
    barchasi_matn = models.CharField(max_length=50, default="Barchasini ko'rish", verbose_name="'Barchasini ko'rish' matni")
    batafsil_matn = models.CharField(max_length=50, default="Batafsil", verbose_name="'Batafsil' matni")
    qadam_matn = models.CharField(max_length=50, default="qadam", verbose_name="'qadam' so'zi")
    joylashuv_matn = models.CharField(max_length=100, default="Joylashuvni aniqlash", verbose_name="Joylashuv tugmasi matni")
    favqulodda_raqamlar_matn = models.CharField(max_length=100, default="Favqulodda raqamlar", verbose_name="'Favqulodda raqamlar' sarlavhasi")
    muhim_badge = models.CharField(max_length=50, default="Muhim", verbose_name="'Muhim' badge matni")
    qidiruv_placeholder = models.CharField(max_length=200, default="Qidirish... (masalan: kuyish, qon ketish)", verbose_name="Qidiruv placeholder")
    xarita_placeholder = models.CharField(max_length=200, default="Xaritani ko'rish uchun joylashuvni aniqlang", verbose_name="Xarita placeholder matni")

    # ============ KATEGORIYA BATAFSIL ============
    shoshilinch_badge = models.CharField(max_length=50, default="SHOSHILINCH", verbose_name="Shoshilinch badge matni")
    muhim_qadam_matn = models.CharField(max_length=200, default="Bu qadam juda muhim!", verbose_name="Muhim qadam ogohlantirish matni")
    boshqa_raqamlar_matn = models.CharField(max_length=100, default="Boshqa raqamlar", verbose_name="'Boshqa raqamlar' matni")
    ovozli_yoriqnoma_matn = models.CharField(max_length=100, default="Ovozli yo'riqnoma", verbose_name="Ovozli yo'riqnoma tugmasi")
    qongiroq_matn = models.CharField(max_length=100, default="GA QO'NG'IROQ QILISH", verbose_name="Qo'ng'iroq tugmasi matni")
    batafsil_oqish_matn = models.CharField(max_length=100, default="Batafsil o'qish", verbose_name="'Batafsil o'qish' matni")

    # ============ SHOSHILINCH SAHIFA ============
    yaqin_kasalxona_matn = models.CharField(max_length=200, default="Eng yaqin kasalxonani topish", verbose_name="Yaqin kasalxona sarlavhasi")
    yaqin_kasalxonalar_btn = models.CharField(max_length=100, default="Yaqin kasalxonalar", verbose_name="Yaqin kasalxonalar tugmasi")
    yaqin_dorixonalar_btn = models.CharField(max_length=100, default="Yaqin dorixonalar", verbose_name="Yaqin dorixonalar tugmasi")

    # ============ VIDEO SAHIFA ============
    barchasi_filter = models.CharField(max_length=50, default="Barchasi", verbose_name="Video filter: Barchasi")
    video_bosh_matn = models.CharField(max_length=200, default="Hozircha video qo'llanmalar qo'shilmagan.", verbose_name="Video bo'sh holat matni")

    # ============ BOLALAR SAHIFA ============
    bolalar_badge = models.CharField(max_length=100, default="Bolalar uchun", verbose_name="Bolalar badge matni")
    bolalar_ogohlantirish_sarlavha = models.CharField(max_length=200, default="Qizil belgili holatlarni bilasizmi?", verbose_name="Bolalar ogohlantirish sarlavhasi")
    bolalar_maslahat_sarlavha = models.CharField(max_length=100, default="Foydali maslahatlar", verbose_name="Bolalar maslahat sarlavhasi")
    barcha_mavzular_matn = models.CharField(max_length=100, default="Barcha mavzular", verbose_name="'Barcha mavzular' matni")
    katalogga_matn = models.CharField(max_length=100, default="Katalogga o'tish", verbose_name="'Katalogga o'tish' tugmasi")

    # ============ DORILAR UI ============
    dori_qoshish_matn = models.CharField(max_length=100, default="Yangi dori qo'shish", verbose_name="Dori qo'shish tugmasi")
    mavjud_dorilar_matn = models.CharField(max_length=100, default="Mavjud dorilar", verbose_name="'Mavjud dorilar' sarlavhasi")
    muddati_xavf_matn = models.CharField(max_length=100, default="Muddati tugash xavfi", verbose_name="Muddati xavf sarlavhasi")
    eslatmalar_matn = models.CharField(max_length=100, default="Eslatmalar", verbose_name="'Eslatmalar' sarlavhasi")
    foydali_maslahat_matn = models.CharField(max_length=100, default="Foydali maslahat", verbose_name="'Foydali maslahat' sarlavhasi")

    # ============ TEST SAHIFA ============
    test_oldingi_matn = models.CharField(max_length=50, default="Oldingi", verbose_name="Test: Oldingi tugma")
    test_keyingi_matn = models.CharField(max_length=50, default="Keyingi", verbose_name="Test: Keyingi tugma")
    test_natija_btn = models.CharField(max_length=100, default="Natijani ko'rish", verbose_name="Test: Natijani ko'rish tugma")
    test_tip_matn = models.CharField(max_length=100, default="Professional tip", verbose_name="Test: Tip sarlavhasi")
    test_ajoyib_matn = models.CharField(max_length=100, default="Ajoyib natija!", verbose_name="Test: Ajoyib natija matni")
    test_yaxshi_matn = models.CharField(max_length=100, default="Yaxshi natija!", verbose_name="Test: Yaxshi natija matni")
    test_orqaning_matn = models.CharField(max_length=100, default="Ko'proq o'rganing!", verbose_name="Test: Ko'proq o'rganing matni")
    test_batafsil_matn = models.CharField(max_length=100, default="Batafsil natijalar", verbose_name="Test: Batafsil natijalar sarlavha")
    test_qayta_matn = models.CharField(max_length=100, default="Qayta topshirish", verbose_name="Test: Qayta topshirish tugma")
    test_bosh_sahifa_matn = models.CharField(max_length=100, default="Bosh sahifaga", verbose_name="Test: Bosh sahifaga tugma")

    # ============ QIDIRUV SAHIFA ============
    qidiruv_sarlavha = models.CharField(max_length=100, default="Qidiruv", verbose_name="Qidiruv sahifa sarlavhasi")
    qidiruv_tavsif = models.CharField(max_length=200, default="Nima bo'lganini yozing - biz yordam beramiz", verbose_name="Qidiruv sahifa tavsifi")
    qidiruv_holatlar_matn = models.CharField(max_length=50, default="Holatlar", verbose_name="Qidiruv: Holatlar sarlavhasi")
    qidiruv_qadamlar_matn = models.CharField(max_length=50, default="Qadamlar", verbose_name="Qidiruv: Qadamlar sarlavhasi")
    qidiruv_btn = models.CharField(max_length=50, default="Qidirish", verbose_name="Qidiruv tugmasi matni")
    qidiruv_bosh_matn = models.CharField(max_length=200, default="bo'yicha natija topilmadi", verbose_name="Qidiruv: natija topilmadi")
    qidiruv_bosh_tavsif = models.CharField(max_length=200, default="Boshqa so'zlar bilan qidirib ko'ring", verbose_name="Qidiruv: boshqa so'zlar matni")

    class Meta:
        verbose_name = "Sayt sozlamalari"
        verbose_name_plural = "Sayt sozlamalari"

    def __str__(self):
        return "Sayt sozlamalari"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    @property
    def hero_rasm_src(self):
        if self.hero_rasm:
            return self.hero_rasm.url
        return self.hero_rasm_url


class Kategoriya(models.Model):
    nomi = models.CharField(max_length=200, verbose_name="Kategoriya nomi")
    icon = models.CharField(max_length=50, verbose_name="Icon (emoji)", default="🏥")
    rang = models.CharField(max_length=7, verbose_name="Rang kodi", default="#e74c3c")
    tartib = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    tavsif = models.TextField(verbose_name="Qisqa tavsif", blank=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['tartib']

    def __str__(self):
        return self.nomi


class Qadam(models.Model):
    kategoriya = models.ForeignKey(
        Kategoriya, on_delete=models.CASCADE,
        related_name='qadamlar', verbose_name="Kategoriya"
    )
    tartib = models.PositiveIntegerField(verbose_name="Qadam raqami")
    sarlavha = models.CharField(max_length=300, verbose_name="Qadam sarlavhasi")
    tavsif = models.TextField(verbose_name="Batafsil tushuntirish", blank=True)
    rasm = models.ImageField(upload_to='qadamlar/', verbose_name="Qadam rasmi", blank=True, null=True)
    muhim = models.BooleanField(default=False, verbose_name="Muhim qadam (qizil)")
    ovozli_matn = models.TextField(
        verbose_name="Ovozli o'qish uchun matn", blank=True,
        help_text="Bo'sh qolsa sarlavha o'qiladi"
    )

    class Meta:
        verbose_name = "Qadam"
        verbose_name_plural = "Qadamlar"
        ordering = ['kategoriya', 'tartib']
        unique_together = ['kategoriya', 'tartib']

    def __str__(self):
        return f"{self.kategoriya.nomi} - Qadam {self.tartib}"


class FavquloddaRaqam(models.Model):
    nomi = models.CharField(max_length=200, verbose_name="Xizmat nomi")
    raqam = models.CharField(max_length=20, verbose_name="Telefon raqami")
    icon = models.CharField(max_length=50, default="📞", verbose_name="Icon")
    asosiy = models.BooleanField(default=False, verbose_name="Asosiy raqam (tez yordam)")
    tartib = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Favqulodda raqam"
        verbose_name_plural = "Favqulodda raqamlar"
        ordering = ['tartib']

    def __str__(self):
        return f"{self.nomi}: {self.raqam}"


class ShoshilinchQadam(models.Model):
    tartib = models.PositiveIntegerField(verbose_name="Qadam raqami")
    sarlavha = models.CharField(max_length=300, verbose_name="Sarlavha")
    tavsif = models.TextField(verbose_name="Tavsif")
    muhim = models.BooleanField(default=False, verbose_name="Muhim qadam (highlighted)")
    qongiroq_tugmasi = models.BooleanField(default=False, verbose_name="Qo'ng'iroq tugmasini ko'rsatish")

    class Meta:
        verbose_name = "Shoshilinch qadam"
        verbose_name_plural = "Shoshilinch qadamlar"
        ordering = ['tartib']

    def __str__(self):
        return f"Qadam {self.tartib}: {self.sarlavha}"


class BolalarOgohlantirish(models.Model):
    matn = models.CharField(max_length=300, verbose_name="Ogohlantirish matni")
    tartib = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Bolalar ogohlantirishи"
        verbose_name_plural = "Bolalar ogohlantirislari"
        ordering = ['tartib']

    def __str__(self):
        return self.matn


class TestSavol(models.Model):
    kategoriya = models.ForeignKey(
        Kategoriya, on_delete=models.CASCADE,
        related_name='savollar', verbose_name="Kategoriya",
        null=True, blank=True
    )
    savol = models.TextField(verbose_name="Savol matni")
    variant_a = models.CharField(max_length=300, verbose_name="A variant")
    variant_b = models.CharField(max_length=300, verbose_name="B variant")
    variant_c = models.CharField(max_length=300, verbose_name="C variant")
    variant_d = models.CharField(max_length=300, verbose_name="D variant")
    togri_javob = models.CharField(
        max_length=1,
        choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')],
        verbose_name="To'g'ri javob"
    )
    izoh = models.TextField(verbose_name="Javob izohi", blank=True)
    rasm = models.ImageField(upload_to='test/', verbose_name="Savol rasmi", blank=True, null=True)

    class Meta:
        verbose_name = "Test savol"
        verbose_name_plural = "Test savollari"

    def __str__(self):
        return self.savol[:80]


class Dori(models.Model):
    foydalanuvchi = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='dorilar', verbose_name="Foydalanuvchi",
        null=True, blank=True,
    )
    nomi = models.CharField(max_length=200, verbose_name="Dori nomi")
    miqdor = models.CharField(max_length=100, verbose_name="Miqdori (masalan: 500mg)", blank=True)
    tavsif = models.TextField(verbose_name="Qisqa tavsif", blank=True)
    rasm = models.ImageField(upload_to='dorilar/', verbose_name="Rasm", blank=True, null=True)
    muddati = models.DateField(verbose_name="Yaroqlilik muddati", blank=True, null=True)
    eslatma_vaqti = models.TimeField(verbose_name="Eslatma vaqti", blank=True, null=True)
    eslatma_kunlar = models.PositiveIntegerField(
        verbose_name="Eslatma davomiyligi (kun)",
        blank=True, null=True,
        help_text="Necha kun davomida eslatib tursin"
    )
    eslatma_tavsif = models.CharField(max_length=300, verbose_name="Eslatma matni", blank=True)
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Dori"
        verbose_name_plural = "Dorilar"
        ordering = ['nomi']

    @property
    def eslatma_faol(self):
        """Eslatma hali davom etyaptimi"""
        if not self.eslatma_vaqti:
            return False
        if not self.eslatma_kunlar:
            return True  # kun belgilanmagan bo'lsa, doim eslatadi
        from django.utils import timezone
        from datetime import timedelta
        tugash = self.qoshilgan_sana + timedelta(days=self.eslatma_kunlar)
        return timezone.now() <= tugash

    @property
    def eslatma_qolgan_kun(self):
        """Eslatma tugashiga necha kun qoldi"""
        if not self.eslatma_vaqti or not self.eslatma_kunlar:
            return None
        from django.utils import timezone
        from datetime import timedelta
        tugash = self.qoshilgan_sana + timedelta(days=self.eslatma_kunlar)
        qolgan = (tugash - timezone.now()).days
        return max(0, qolgan)

    def __str__(self):
        return f"{self.nomi} {self.miqdor}"


class VideoQollanma(models.Model):
    sarlavha = models.CharField(max_length=300, verbose_name="Video sarlavhasi")
    tavsif = models.TextField(verbose_name="Qisqa tavsif", blank=True)
    youtube_url = models.URLField(verbose_name="YouTube havolasi", blank=True)
    video_fayl = models.FileField(upload_to='videolar/fayllar/', verbose_name="Video fayl (MP4)", blank=True, null=True)
    rasm = models.ImageField(upload_to='videolar/', verbose_name="Custom thumbnail", blank=True, null=True)
    kategoriya = models.ForeignKey(
        Kategoriya, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="Kategoriya"
    )
    tartib = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Video qo'llanma"
        verbose_name_plural = "Video qo'llanmalar"
        ordering = ['tartib']

    def __str__(self):
        return self.sarlavha

    @property
    def is_local(self):
        return bool(self.video_fayl)

    @property
    def youtube_id(self):
        url = self.youtube_url
        if not url:
            return ''
        if 'youtu.be/' in url:
            return url.split('youtu.be/')[-1].split('?')[0]
        if 'watch?v=' in url:
            return url.split('watch?v=')[-1].split('&')[0]
        if 'embed/' in url:
            return url.split('embed/')[-1].split('?')[0]
        return url

    @property
    def thumbnail(self):
        if self.rasm:
            return self.rasm.url
        if self.youtube_id:
            return f"https://img.youtube.com/vi/{self.youtube_id}/hqdefault.jpg"
        return ''


class BolalarMavzu(models.Model):
    sarlavha = models.CharField(max_length=300, verbose_name="Mavzu sarlavhasi")
    tavsif = models.TextField(verbose_name="Tavsif")
    rasm = models.ImageField(upload_to='bolalar/', verbose_name="Rasm", blank=True, null=True)
    icon = models.CharField(max_length=50, verbose_name="Icon (emoji)", default="🧒")
    tartib = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    tanlangan = models.BooleanField(default=False, verbose_name="Asosiy mavzu (featured)")

    class Meta:
        verbose_name = "Bolalar mavzusi"
        verbose_name_plural = "Bolalar mavzulari"
        ordering = ['tartib']

    def __str__(self):
        return self.sarlavha


class BolalarMalumot(models.Model):
    sarlavha = models.CharField(max_length=200, verbose_name="Sarlavha")
    matn = models.TextField(verbose_name="Matn")
    icon = models.CharField(max_length=50, verbose_name="Icon (emoji)", default="📌")
    rang = models.CharField(max_length=7, verbose_name="Rang kodi", default="#3b82f6")
    tartib = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Bolalar ma'lumoti"
        verbose_name_plural = "Bolalar ma'lumotlari"
        ordering = ['tartib']

    def __str__(self):
        return self.sarlavha


class TelegramFoydalanuvchi(models.Model):
    foydalanuvchi = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='telegram', verbose_name="Foydalanuvchi",
        null=True, blank=True,
    )
    telegram_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")
    ism = models.CharField(max_length=200, verbose_name="Ism", blank=True)
    username = models.CharField(max_length=200, verbose_name="Username", blank=True)
    faol = models.BooleanField(default=True, verbose_name="Faol")
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Telegram foydalanuvchi"
        verbose_name_plural = "Telegram foydalanuvchilar"

    def __str__(self):
        return f"{self.ism} (@{self.username})" if self.username else f"{self.ism} ({self.telegram_id})"


class TelegramUlanishTokeni(models.Model):
    foydalanuvchi = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='telegram_token'
    )
    token = models.CharField(max_length=32, unique=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Telegram ulanish tokeni"
        verbose_name_plural = "Telegram ulanish tokenlari"

    def __str__(self):
        return f"{self.foydalanuvchi} - {self.token}"


class BolalarQadam(models.Model):
    mavzu = models.ForeignKey(
        BolalarMavzu, on_delete=models.CASCADE,
        related_name='qadamlar', verbose_name="Mavzu"
    )
    tartib = models.PositiveIntegerField(verbose_name="Qadam raqami")
    matn = models.TextField(verbose_name="Qadam matni")

    class Meta:
        verbose_name = "Bolalar qadami"
        verbose_name_plural = "Bolalar qadamlari"
        ordering = ['mavzu', 'tartib']

    def __str__(self):
        return f"{self.mavzu.sarlavha} - Qadam {self.tartib}"
