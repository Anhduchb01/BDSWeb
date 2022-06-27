from attr import field
from rest_framework import serializers
from .models import Data
class GetAllBaidang(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields =['id_baidang','nhu_cau','chuyen_muc','tinh_tp','quan_huyen','tt_phap_ly','gia','dien_tich']