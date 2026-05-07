from .models import SaytSozlamalari, FavquloddaRaqam


def sayt_sozlamalari(request):
    sozlamalar = SaytSozlamalari.load()
    asosiy_raqam = FavquloddaRaqam.objects.filter(asosiy=True).first()
    return {
        's': sozlamalar,
        'asosiy_raqam': asosiy_raqam,
    }
