from django.contrib import admin
from .models import (
    SaytSozlamalari, Kategoriya, Qadam, FavquloddaRaqam, ShoshilinchQadam,
    BolalarOgohlantirish, TestSavol, Dori, VideoQollanma, BolalarMavzu, BolalarQadam,
    TelegramFoydalanuvchi, BolalarMalumot
)


@admin.register(SaytSozlamalari)
class SaytSozlamalariAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Umumiy', {'fields': ('sayt_nomi', 'logo_matn', 'footer_matn')}),
        ('Bosh sahifa - Hero', {'fields': (
            'hero_sarlavha', 'hero_tavsif', 'hero_rasm', 'hero_rasm_url',
            'hero_tugma1_matn', 'hero_tugma2_matn',
            'hero_stat_sarlavha', 'hero_stat_tavsif',
        )}),
        ('Bosh sahifa - Qizil divider', {'fields': (
            'divider_1_raqam', 'divider_1_matn',
            'divider_2_raqam', 'divider_2_matn',
            'divider_3_raqam', 'divider_3_matn',
        )}),
        ('Bosh sahifa - Kategoriyalar', {'fields': ('kategoriya_badge', 'kategoriya_sarlavha')}),
        ('Bosh sahifa - Xarita', {'fields': ('xarita_badge', 'xarita_sarlavha', 'xarita_tavsif')}),
        ('Bosh sahifa - Promo', {'fields': (
            'promo_badge', 'promo_sarlavha', 'promo_tavsif', 'promo_tugma_matn',
            'promo_stat1_raqam', 'promo_stat1_label', 'promo_stat2_raqam', 'promo_stat2_label',
        )}),
        ('Katalog sahifasi', {'fields': (
            'katalog_badge', 'katalog_sarlavha', 'katalog_tavsif', 'katalog_rasm',
            'katalog_protokol_sarlavha', 'katalog_protokol_tavsif',
        )}),
        ('Shoshilinch sahifa', {'fields': ('shoshilinch_sarlavha', 'shoshilinch_tavsif')}),
        ('Video sahifasi', {'fields': ('video_sarlavha', 'video_tavsif')}),
        ('Bolalar sahifasi', {'fields': (
            'bolalar_sarlavha', 'bolalar_tavsif', 'bolalar_maslahat',
            'bolalar_cta_sarlavha', 'bolalar_cta_tavsif',
        )}),
        ('Dorilar sahifasi', {'fields': ('dorilar_sarlavha', 'dorilar_tavsif', 'dorilar_maslahat')}),
        ('Navigatsiya va Footer', {
            'classes': ('collapse',),
            'fields': (
                'nav_home', 'nav_catalog', 'nav_quiz', 'nav_emergency',
                'footer_havola1', 'footer_havola2', 'footer_havola3', 'footer_havola4',
            ),
        }),
        ('Umumiy UI matnlari', {
            'classes': ('collapse',),
            'fields': (
                'barchasi_matn', 'batafsil_matn', 'qadam_matn', 'joylashuv_matn',
                'favqulodda_raqamlar_matn', 'muhim_badge', 'qidiruv_placeholder', 'xarita_placeholder',
            ),
        }),
        ('Kategoriya batafsil sahifasi', {
            'classes': ('collapse',),
            'fields': (
                'shoshilinch_badge', 'muhim_qadam_matn', 'boshqa_raqamlar_matn',
                'ovozli_yoriqnoma_matn', 'qongiroq_matn', 'batafsil_oqish_matn',
            ),
        }),
        ('Shoshilinch sahifa UI', {
            'classes': ('collapse',),
            'fields': (
                'yaqin_kasalxona_matn', 'yaqin_kasalxonalar_btn', 'yaqin_dorixonalar_btn',
            ),
        }),
        ('Video sahifa UI', {
            'classes': ('collapse',),
            'fields': ('barchasi_filter', 'video_bosh_matn'),
        }),
        ('Bolalar sahifa UI', {
            'classes': ('collapse',),
            'fields': (
                'bolalar_badge', 'bolalar_ogohlantirish_sarlavha', 'bolalar_maslahat_sarlavha',
                'barcha_mavzular_matn', 'katalogga_matn',
            ),
        }),
        ('Dorilar sahifa UI', {
            'classes': ('collapse',),
            'fields': (
                'dori_qoshish_matn', 'mavjud_dorilar_matn', 'muddati_xavf_matn',
                'eslatmalar_matn', 'foydali_maslahat_matn',
            ),
        }),
        ('Test sahifa UI', {
            'classes': ('collapse',),
            'fields': (
                'test_oldingi_matn', 'test_keyingi_matn', 'test_natija_btn', 'test_tip_matn',
                'test_ajoyib_matn', 'test_yaxshi_matn', 'test_orqaning_matn',
                'test_batafsil_matn', 'test_qayta_matn', 'test_bosh_sahifa_matn',
            ),
        }),
        ('Qidiruv sahifa UI', {
            'classes': ('collapse',),
            'fields': (
                'qidiruv_sarlavha', 'qidiruv_tavsif', 'qidiruv_holatlar_matn',
                'qidiruv_qadamlar_matn', 'qidiruv_btn', 'qidiruv_bosh_matn', 'qidiruv_bosh_tavsif',
            ),
        }),
    )

    def has_add_permission(self, request):
        return not SaytSozlamalari.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class QadamInline(admin.TabularInline):
    model = Qadam
    extra = 1
    ordering = ['tartib']


@admin.register(Kategoriya)
class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'icon', 'tartib']
    inlines = [QadamInline]


@admin.register(Qadam)
class QadamAdmin(admin.ModelAdmin):
    list_display = ['kategoriya', 'tartib', 'sarlavha', 'muhim']
    list_filter = ['kategoriya', 'muhim']


@admin.register(FavquloddaRaqam)
class FavquloddaRaqamAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'raqam', 'icon', 'asosiy', 'tartib']
    list_editable = ['asosiy', 'tartib']


@admin.register(ShoshilinchQadam)
class ShoshilinchQadamAdmin(admin.ModelAdmin):
    list_display = ['tartib', 'sarlavha', 'muhim', 'qongiroq_tugmasi']
    list_editable = ['muhim', 'qongiroq_tugmasi']
    ordering = ['tartib']


@admin.register(BolalarOgohlantirish)
class BolalarOgohlantirishAdmin(admin.ModelAdmin):
    list_display = ['matn', 'tartib']
    list_editable = ['tartib']


class TestSavolAdmin(admin.ModelAdmin):
    list_display = ['savol', 'kategoriya', 'togri_javob']
    list_filter = ['kategoriya']


admin.site.register(TestSavol, TestSavolAdmin)


@admin.register(Dori)
class DoriAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'miqdor', 'muddati', 'eslatma_vaqti', 'eslatma_kunlar']
    list_filter = ['muddati']


@admin.register(VideoQollanma)
class VideoQollanmaAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'kategoriya', 'tartib', 'is_local']
    list_filter = ['kategoriya']

    def is_local(self, obj):
        return bool(obj.video_fayl)
    is_local.boolean = True
    is_local.short_description = 'Lokal video'


class BolalarQadamInline(admin.TabularInline):
    model = BolalarQadam
    extra = 1
    ordering = ['tartib']


@admin.register(BolalarMavzu)
class BolalarMavzuAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'icon', 'tartib', 'tanlangan']
    list_filter = ['tanlangan']
    inlines = [BolalarQadamInline]


@admin.register(BolalarMalumot)
class BolalarMalumotAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'icon', 'tartib']
    list_editable = ['tartib']


@admin.register(TelegramFoydalanuvchi)
class TelegramFoydalanuvchiAdmin(admin.ModelAdmin):
    list_display = ['ism', 'username', 'telegram_id', 'faol', 'qoshilgan_sana']
    list_filter = ['faol']
    search_fields = ['ism', 'username']


admin.site.site_header = "FirstAid.uz - Admin"
admin.site.site_title = "FirstAid.uz Admin"
