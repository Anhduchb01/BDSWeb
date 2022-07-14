
import random
from unicodedata import decimal
from django.http import JsonResponse

from django.shortcuts import render,HttpResponse,redirect 
from django.views import View
from requests import request
from sympy import N
from .models import Data,DevvnTinhthanhpho,DevvnQuanhuyen,Nguoidang,Daluu
from django.contrib.auth import authenticate,login,logout,decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GetAllBaidang

from django.conf import settings


# Create your views here.
class GetAllAPIBaidang(APIView):
    def get(self, request):
        list_baidang = Data.objects.all()
        mydata = GetAllBaidang(list_baidang,many=True)
        return Response(data=mydata.data,status=status.HTTP_200_OK)
class HomeView(View):
    def get(self, request):
        list_baidang_index = list(Data.objects.exclude(img__isnull=True).exclude(img__exact=''))

        random_baidang_index = random.sample(list_baidang_index, 3)
        context_index = {'dsbaidang': random_baidang_index,'media_url':settings.MEDIA_URL}
        return render(request,'homepage/index.html',context_index)
class TimKiem(View):
    def get(self, request):
        list_tinhtp = list(DevvnTinhthanhpho.objects.all())     
        list_baidang = list(Data.objects.exclude(img__isnull=True).exclude(img__exact=''))
        random_baidang = random.sample(list_baidang, 9)
        context = {'dsbaidang': random_baidang, 'dstinhtp' : list_tinhtp}
        return render(request,'homepage/timkiem.html',context)
class load_quanhuyen(View):
    def get(self ,request):
        
        province_id = request.GET.get('province_id')
        listquanhuyen = DevvnQuanhuyen.objects.filter(matp=province_id)
        return render(request, 'homepage/quanhuyen_dropdown_list_options.html', {'listquanhuyen': listquanhuyen})
class daluu(View):
    def get(self,request,username):
        
        
        listid_baidang = Daluu.objects.filter(username=username).values('id_baidang')
        listbaidang1 = Data.objects.filter(id_baidang__in=listid_baidang)
        p = Paginator(listbaidang1, 9)
        page = request.GET.get('page')
        
        venues = p.get_page(page)
        context = {'dsbaidang': venues}
        
        return render(request,'homepage/daluu.html',context)

              
class LoadTimKiem(View):
    def get(self,request):
        chuyenmuc = request.GET.get('chuyen_muc')
        gia = request.GET.get('gia')
        dien_tich = request.GET.get('dien_tich')
        tinh_tp = request.GET.get('s_province_id')
        quan_huyen = request.GET.get('s_district_id')
        list_tinhtp = list(DevvnTinhthanhpho.objects.all())
        list_baidang = Data.objects.all()
        
        
        
        if chuyenmuc is not None and chuyenmuc != '0':
            list_baidang = list_baidang.filter(chuyen_muc = chuyenmuc)
        if gia is not None and gia != '0':
            
            gia = int(gia)
            don_vi = 'Tỷ'
            if gia ==1 :
                gia_min = 0
                gia_max = 500
                don_vi = 'Triệu'
            elif gia ==2:
                gia_min = 500
                gia_max = 800
                don_vi = 'Triệu'
            elif gia ==3:
                gia_min = 800
                gia_max = 1000
                don_vi = 'Triệu'
            elif gia ==4:
                gia_min = 1
                gia_max = 2
                
            elif gia ==5:
                gia_min = 2
                gia_max = 3
                
            elif gia ==6:
                gia_min = 3
                gia_max = 5
            elif gia ==7:
                gia_min = 5
                gia_max = 8
            elif gia ==8:
                gia_min = 8
                gia_max = 10
            elif gia ==9:
                gia_min = 10
                gia_max = 20
            elif gia == 10:
                gia_min = 20
                gia_max = 30
            else:
                gia_min =30
                gia_max = 1000
            list_baidang = list_baidang.filter(donvi_gia=don_vi,gia_tien__gte=gia_min, gia_tien__lte=gia_max)
        if dien_tich is not None and dien_tich != '0':
            dien_tich = int(dien_tich)
            if dien_tich ==30:
                dien_tich_min = 0
                dien_tich_max = 30
            elif dien_tich ==50:
                dien_tich_min = 30
                dien_tich_max = 50
            elif dien_tich ==80:
                dien_tich_min = 50
                dien_tich_max = 80
            elif dien_tich ==100:
                dien_tich_min = 80
                dien_tich_max = 100
            elif dien_tich ==150:
                dien_tich_min = 100
                dien_tich_max = 150
            elif dien_tich ==200:
                dien_tich_min = 150
                dien_tich_max = 200
            elif dien_tich ==250:
                dien_tich_min = 200
                dien_tich_max = 250
            elif dien_tich ==300:
                dien_tich_min = 250
                dien_tich_max = 300
            elif dien_tich ==500:
                dien_tich_min = 300
                dien_tich_max = 500
            else:
                dien_tich_min = 500
                dien_tich_max = 10000
            list_baidang = list_baidang.filter(dien_tich1__gte=dien_tich_min, dien_tich1__lte=dien_tich_max)
        ds_quanhuyen = ''
        if tinh_tp is not None and tinh_tp != '0':
            name_tinh_tp = DevvnTinhthanhpho.objects.get(matp=tinh_tp)
            name_tinh = name_tinh_tp.name
            name_tinh = name_tinh.replace('Thành phố ', '')
            name_tinh = name_tinh.replace('Tỉnh ', '')
            ds_quanhuyen = DevvnQuanhuyen.objects.filter(matp=tinh_tp)
            
            
            list_baidang = list_baidang.filter(tinh_tp=name_tinh)
        
        if quan_huyen is not None and quan_huyen != 'None' and quan_huyen != '0': 
            name_quan_huyen = DevvnQuanhuyen.objects.get(maqh=quan_huyen)
            ds_quanhuyen = DevvnQuanhuyen.objects.filter(matp=tinh_tp)
            name_quanhuyen1 = name_quan_huyen.name
            name_quanhuyen1 = name_quanhuyen1.replace('Quận ', '')
            name_quanhuyen1 = name_quanhuyen1.replace('Huyện ', '')
            list_baidang = list_baidang.filter(quan_huyen__contains=name_quanhuyen1)
            
                


           
        p = Paginator(list_baidang, 9)
        page = request.GET.get('page')
        
        venues = p.get_page(page)
        context = {'dsbaidang': venues, 'dstinhtp' : list_tinhtp,'dsquanhuyen':ds_quanhuyen ,'chuyen_muc' :chuyenmuc,'gia':gia,'dien_tich':dien_tich,'tinh_tp':tinh_tp,'quan_huyen':quan_huyen}
        
        return render(request,'homepage/timkiem.html',context)
class Baidang(View):
    def get(self,request,id):
        id_baidang = id
        user1= request.user.username
       
        list_baidang1 = Data.objects.all().extra(select={'nguoidang': 'nguoidang.nguoi_dang','sdt':'nguoidang.sdt','so_like':'nguoidang.so_like','id_nguoidang':'nguoidang.id_nguoidang'},
    tables=['nguoidang'],
    where=['Data.id_nguoidang=nguoidang.id_nguoidang'])
        list_baidang = list_baidang1.get(id_baidang=id_baidang)
        so_like = round(list_baidang.so_like)
        if  Daluu.objects.filter(id_baidang=id_baidang,username=user1).exists():
            daluuchua =True
        else :
            daluuchua = False
        
        context ={'dsbaidang':list_baidang,'so_like':so_like,'daluuchua':daluuchua}
        return render(request,'homepage/detailbaidang.html',context)
    
def dangnhap(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'homepage/login.html', context)

def dangxuat(request):
    logout(request)
    return redirect('index')
       
        
def dangky(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
        context = {'form':form}
        return render(request, 'homepage/dangky.html', context)

def updatestar(request):
    
        
    data = {'response': ''}

    selected_star = request.GET.get('value')
    id_nguoidang = request.GET.get('id_nguoidang')
            
    nguoidang = Nguoidang.objects.get(id_nguoidang=id_nguoidang)
            
    pre_so_like = nguoidang.so_like
    pre_so_vote = nguoidang.so_vote
    nguoidang.so_vote = pre_so_vote +1
    new_like = (float(pre_so_like)*float(pre_so_vote) + float(selected_star))/(float(pre_so_vote) + 1 )
    nguoidang.so_like =new_like 
    nguoidang.save()
    data['response'] = 'Record updated!' 
    return  JsonResponse(data)
def luubaidang(request):
    
        data = {'response': ''}
        username= request.GET.get('user_name')
        id_baidang= request.GET.get('id_baidang')
        if Daluu.objects.filter(username=username,id_baidang=id_baidang).exists():
            pass
        else:
            Daluu.objects.create(username=username,id_baidang=id_baidang)
            data['response'] = 'Record updated!' 
            return  JsonResponse(data)

            

        









    