
from django.urls import path
from .views import HomeView,TimKiem,load_quanhuyen,LoadTimKiem,Baidang,GetAllAPIBaidang, luubaidang,updatestar,daluu
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', HomeView.as_view(),name='index'),
    path('timkiem', TimKiem.as_view(), name='timkiem'),
    path('ajax/load-quanhuyen/', load_quanhuyen.as_view(), name='ajax_load_quanhuyen'),
    path('timkiem/load',LoadTimKiem.as_view(), name="loadtimkiem"), 
    path('login',views.dangnhap, name="login"),
    path('dangky',views.dangky, name="dangky"),  
    path('dangxuat',views.dangxuat, name="dangxuat"),
    path('<int:id>',Baidang.as_view(), name="baidang"),
    path('Getbaidang/',GetAllAPIBaidang.as_view()),
    path('updatestar',views.updatestar,name='updatestar'),
    path('daluu/<str:username>',daluu.as_view(),name='daluu'),
    path('luubaidang',views.luubaidang,name='luubaidang')
]