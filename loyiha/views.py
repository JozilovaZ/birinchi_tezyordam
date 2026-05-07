import secrets

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import date
from .forms import RoyxatdanOtishForm, KirishForm
from .models import (
    Kategoriya, Qadam, FavquloddaRaqam, TestSavol, Dori,
    VideoQollanma, BolalarMavzu, BolalarOgohlantirish, ShoshilinchQadam,
    TelegramUlanishTokeni, BolalarMalumot, BolalarQadam,
)


def bosh_sahifa(request):
    kategoriyalar = Kategoriya.objects.all()
    raqamlar = FavquloddaRaqam.objects.all()
    return render(request, 'loyiha/bosh_sahifa.html', {
        'kategoriyalar': kategoriyalar,
        'raqamlar': raqamlar,
    })


def katalog(request):
    kategoriyalar = Kategoriya.objects.all()
    raqamlar = FavquloddaRaqam.objects.all()
    return render(request, 'loyiha/katalog.html', {
        'kategoriyalar': kategoriyalar,
        'raqamlar': raqamlar,
    })


def kategoriya_batafsil(request, pk):
    kategoriya = get_object_or_404(Kategoriya, pk=pk)
    qadamlar = kategoriya.qadamlar.all()
    raqamlar = FavquloddaRaqam.objects.all()
    return render(request, 'loyiha/kategoriya_batafsil.html', {
        'kategoriya': kategoriya,
        'qadamlar': qadamlar,
        'raqamlar': raqamlar,
    })


def shoshilinch(request):
    raqamlar = FavquloddaRaqam.objects.all()
    kategoriyalar = Kategoriya.objects.all()[:6]
    qadamlar = ShoshilinchQadam.objects.all()
    return render(request, 'loyiha/shoshilinch.html', {
        'raqamlar': raqamlar,
        'kategoriyalar': kategoriyalar,
        'qadamlar': qadamlar,
    })


def qidiruv(request):
    query = request.GET.get('q', '').strip()
    natijalar = []
    if query:
        natijalar = Kategoriya.objects.filter(
            Q(nomi__icontains=query) | Q(tavsif__icontains=query)
        )
        qadam_natijalar = Qadam.objects.filter(
            Q(sarlavha__icontains=query) | Q(tavsif__icontains=query)
        ).select_related('kategoriya')

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = []
            for k in natijalar:
                data.append({'id': k.id, 'nomi': k.nomi, 'icon': k.icon, 'tur': 'kategoriya'})
            for q in qadam_natijalar:
                data.append({
                    'id': q.kategoriya.id,
                    'nomi': f"{q.kategoriya.nomi}: {q.sarlavha}",
                    'icon': q.kategoriya.icon,
                    'tur': 'qadam'
                })
            return JsonResponse(data, safe=False)
    else:
        qadam_natijalar = []

    return render(request, 'loyiha/qidiruv.html', {
        'query': query,
        'natijalar': natijalar,
        'qadam_natijalar': qadam_natijalar,
    })


def test_sahifa(request):
    savollar = TestSavol.objects.all().order_by('?')[:50]
    return render(request, 'loyiha/test.html', {
        'savollar': savollar,
    })


def test_tekshir(request):
    if request.method == 'POST':
        savollar = TestSavol.objects.all()
        togri = 0
        jami = 0
        natijalar = []
        for savol in savollar:
            javob = request.POST.get(f'savol_{savol.id}')
            if javob:
                jami += 1
                is_correct = javob == savol.togri_javob
                if is_correct:
                    togri += 1
                natijalar.append({
                    'savol': savol,
                    'javob': javob,
                    'togri': savol.togri_javob,
                    'is_correct': is_correct,
                })
        foiz = round(togri / jami * 100) if jami > 0 else 0
        return render(request, 'loyiha/test_natija.html', {
            'togri': togri,
            'jami': jami,
            'foiz': foiz,
            'natijalar': natijalar,
        })
    return render(request, 'loyiha/test.html', {'savollar': TestSavol.objects.all()})


@login_required(login_url='loyiha:kirish')
def dorilar(request):
    dorilar = Dori.objects.filter(foydalanuvchi=request.user)
    bugun = date.today()
    try:
        next_month = bugun.replace(month=bugun.month + 1)
    except ValueError:
        next_month = bugun.replace(year=bugun.year + 1, month=1)
    xavfli_dorilar = dorilar.filter(muddati__isnull=False, muddati__lte=next_month)
    eslatmalar = dorilar.filter(eslatma_vaqti__isnull=False).order_by('eslatma_vaqti')

    telegram_ulangan = hasattr(request.user, 'telegram')
    ulanish_linki = None
    if not telegram_ulangan:
        token_obj, _ = TelegramUlanishTokeni.objects.get_or_create(
            foydalanuvchi=request.user,
            defaults={'token': secrets.token_urlsafe(12)}
        )
        ulanish_linki = f"https://t.me/{settings.TELEGRAM_BOT_USERNAME}?start={token_obj.token}"

    return render(request, 'loyiha/dorilar.html', {
        'dorilar': dorilar,
        'xavfli_dorilar': xavfli_dorilar,
        'eslatmalar': eslatmalar,
        'telegram_bot_username': settings.TELEGRAM_BOT_USERNAME,
        'telegram_ulangan': telegram_ulangan,
        'ulanish_linki': ulanish_linki,
    })


@login_required(login_url='loyiha:kirish')
def dori_qoshish(request):
    if request.method == 'POST':
        nomi = request.POST.get('nomi', '')
        miqdor = request.POST.get('miqdor', '')
        tavsif = request.POST.get('tavsif', '')
        muddati = request.POST.get('muddati', '') or None
        eslatma_vaqti = request.POST.get('eslatma_vaqti', '') or None
        eslatma_kunlar = request.POST.get('eslatma_kunlar', '') or None
        if eslatma_kunlar:
            eslatma_kunlar = int(eslatma_kunlar)
        eslatma_tavsif = request.POST.get('eslatma_tavsif', '')
        rasm = request.FILES.get('rasm')
        Dori.objects.create(
            foydalanuvchi=request.user,
            nomi=nomi,
            miqdor=miqdor,
            tavsif=tavsif,
            muddati=muddati,
            eslatma_vaqti=eslatma_vaqti,
            eslatma_kunlar=eslatma_kunlar,
            eslatma_tavsif=eslatma_tavsif,
            rasm=rasm,
        )
        return redirect('loyiha:dorilar')
    return redirect('loyiha:dorilar')


@login_required(login_url='loyiha:kirish')
def dori_ochirish(request, pk):
    if request.method == 'POST':
        dori = get_object_or_404(Dori, pk=pk, foydalanuvchi=request.user)
        dori.delete()
    return redirect('loyiha:dorilar')


def royxatdan_otish(request):
    if request.user.is_authenticated:
        return redirect('loyiha:bosh_sahifa')
    if request.method == 'POST':
        form = RoyxatdanOtishForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('loyiha:dorilar')
    else:
        form = RoyxatdanOtishForm()
    return render(request, 'loyiha/royxatdan_otish.html', {'form': form})


def kirish(request):
    if request.user.is_authenticated:
        return redirect('loyiha:bosh_sahifa')
    if request.method == 'POST':
        form = KirishForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            keyin = request.GET.get('next') or request.POST.get('next')
            return redirect(keyin or 'loyiha:dorilar')
    else:
        form = KirishForm(request)
    return render(request, 'loyiha/kirish.html', {'form': form})


def chiqish(request):
    logout(request)
    return redirect('loyiha:bosh_sahifa')


def videolar(request):
    videolar = VideoQollanma.objects.all()
    kategoriyalar = Kategoriya.objects.all()
    tanlangan_kat = request.GET.get('kategoriya')
    if tanlangan_kat:
        videolar = videolar.filter(kategoriya_id=tanlangan_kat)
    return render(request, 'loyiha/videolar.html', {
        'videolar': videolar,
        'kategoriyalar': kategoriyalar,
        'tanlangan_kat': tanlangan_kat,
    })


def bolalar(request):
    mavzular = BolalarMavzu.objects.all()
    tanlangan = BolalarMavzu.objects.filter(tanlangan=True).first()
    ogohlantirishlar = BolalarOgohlantirish.objects.all()
    malumotlar = BolalarMalumot.objects.all()
    return render(request, 'loyiha/bolalar.html', {
        'mavzular': mavzular,
        'tanlangan': tanlangan,
        'ogohlantirishlar': ogohlantirishlar,
        'malumotlar': malumotlar,
    })


def bolalar_mavzu(request, pk):
    mavzu = get_object_or_404(BolalarMavzu, pk=pk)
    qadamlar = mavzu.qadamlar.all().order_by('tartib')
    boshqa_mavzular = BolalarMavzu.objects.exclude(pk=pk)[:5]
    return render(request, 'loyiha/bolalar_mavzu.html', {
        'mavzu': mavzu,
        'qadamlar': qadamlar,
        'boshqa_mavzular': boshqa_mavzular,
    })


def simulyatsiya(request):
    kategoriyalar = Kategoriya.objects.prefetch_related('qadamlar').all()
    kategoriya_id = request.GET.get('kategoriya')
    tanlangan = None
    videolar = []
    if kategoriya_id:
        tanlangan = get_object_or_404(Kategoriya, pk=kategoriya_id)
        videolar = VideoQollanma.objects.filter(kategoriya=tanlangan)
    return render(request, 'loyiha/simulyatsiya.html', {
        'kategoriyalar': kategoriyalar,
        'tanlangan': tanlangan,
        'videolar': videolar,
    })


def simulyatsiya_tekshir(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        kategoriya_id = data.get('kategoriya_id')
        user_order = data.get('tartib', [])
        kategoriya = get_object_or_404(Kategoriya, pk=kategoriya_id)
        qadamlar = list(kategoriya.qadamlar.order_by('tartib').values_list('id', flat=True))
        togri = 0
        natijalar = []
        for i, qadam_id in enumerate(user_order):
            qadam_id = int(qadam_id)
            is_correct = i < len(qadamlar) and qadam_id == qadamlar[i]
            if is_correct:
                togri += 1
            qadam = kategoriya.qadamlar.get(id=qadam_id)
            natijalar.append({
                'id': qadam.id,
                'sarlavha': qadam.sarlavha,
                'togri_tartib': qadamlar.index(qadam_id) + 1 if qadam_id in qadamlar else 0,
                'user_tartib': i + 1,
                'is_correct': is_correct,
            })
        foiz = round(togri / len(qadamlar) * 100) if qadamlar else 0
        return JsonResponse({
            'togri': togri,
            'jami': len(qadamlar),
            'foiz': foiz,
            'natijalar': natijalar,
        })
    return JsonResponse({'error': 'POST only'}, status=400)
