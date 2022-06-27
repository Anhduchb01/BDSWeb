
from django.urls import path
from .views import HomeView,TimKiem,load_quanhuyen,LoadTimKiem,Baidang,GetAllAPIBaidang
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
    path('Getbaidang/',GetAllAPIBaidang.as_view())
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 