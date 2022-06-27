from distutils.command.upload import upload
from django.db import models


class Nguoidang(models.Model):
    id_nguoidang = models.IntegerField(primary_key=True)
    nguoi_dang = models.TextField(blank=True, null=True)
    sdt = models.TextField(blank=True, null=True)
    so_like = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nguoidang'
# Create your models here.
class Data(models.Model):
    
    id_baidang = models.IntegerField(primary_key=True)
    nhu_cau = models.TextField(blank=True, null=True)
    chuyen_muc = models.TextField(blank=True, null=True)
    tinh_tp = models.TextField(blank=True, null=True)
    quan_huyen = models.TextField(blank=True, null=True)
    phuong_xa = models.TextField(blank=True, null=True)
    tt_phap_ly = models.TextField(blank=True, null=True)
    gia = models.TextField(blank=True, null=True)
    gia_tien = models.FloatField(blank=True, null=True)
    donvi_gia = models.TextField(blank=True, null=True)
    dien_tich = models.TextField(blank=True, null=True)
    dien_tich1 = models.FloatField()
    mo_ta = models.TextField(blank=True, null=True)
    id_nguoidang = models.IntegerField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True,upload_to ="baidang/")

    class Meta:
        managed = False
        db_table = 'data'
    def __str__(self):
        return 'Bài đăng id: '+ str(self.id_baidang)
            

class DevvnQuanhuyen(models.Model):
    maqh = models.CharField(primary_key=True, max_length=5, db_collation='utf8_general_ci')
    name = models.CharField(max_length=100, db_collation='utf8_general_ci')
    type = models.CharField(max_length=30, db_collation='utf8_general_ci')
    matp = models.CharField(max_length=5, db_collation='utf8_general_ci')

    class Meta:
        managed = False
        db_table = 'devvn_quanhuyen'


class DevvnTinhthanhpho(models.Model):
    matp = models.CharField(primary_key=True, max_length=5, db_collation='utf8_general_ci')
    name = models.CharField(max_length=100, db_collation='utf8_general_ci')
    type = models.CharField(max_length=30, db_collation='utf8_general_ci')
    slug = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devvn_tinhthanhpho'


class DevvnXaphuongthitran(models.Model):
    xaid = models.CharField(primary_key=True, max_length=5, db_collation='utf8_general_ci')
    name = models.CharField(max_length=100, db_collation='utf8_general_ci')
    type = models.CharField(max_length=30, db_collation='utf8_general_ci')
    maqh = models.CharField(max_length=5, db_collation='utf8_general_ci')

    class Meta:
        managed = False
        db_table = 'devvn_xaphuongthitran'
