from django.urls import path
from . import views

app_name = 'loyiha'

urlpatterns = [
    path('', views.bosh_sahifa, name='bosh_sahifa'),
    path('katalog/', views.katalog, name='katalog'),
    path('holat/<int:pk>/', views.kategoriya_batafsil, name='kategoriya_batafsil'),
    path('shoshilinch/', views.shoshilinch, name='shoshilinch'),
    path('qidiruv/', views.qidiruv, name='qidiruv'),
    path('test/', views.test_sahifa, name='test'),
    path('test/tekshir/', views.test_tekshir, name='test_tekshir'),
    path('dorilar/', views.dorilar, name='dorilar'),
    path('dorilar/qoshish/', views.dori_qoshish, name='dori_qoshish'),
    path('dorilar/ochirish/<int:pk>/', views.dori_ochirish, name='dori_ochirish'),
    path('kirish/', views.kirish, name='kirish'),
    path('royxatdan-otish/', views.royxatdan_otish, name='royxatdan_otish'),
    path('chiqish/', views.chiqish, name='chiqish'),
    path('videolar/', views.videolar, name='videolar'),
    path('bolalar/', views.bolalar, name='bolalar'),
    path('bolalar/<int:pk>/', views.bolalar_mavzu, name='bolalar_mavzu'),
    path('simulyatsiya/', views.simulyatsiya, name='simulyatsiya'),
    path('simulyatsiya/tekshir/', views.simulyatsiya_tekshir, name='simulyatsiya_tekshir'),
]
