# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    id_nguoidang = models.IntegerField()
    img = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'


class Data2(models.Model):
    id_baidang = models.AutoField(primary_key=True)
    nhu_cau = models.TextField(blank=True, null=True)
    chuyen_muc = models.TextField(blank=True, null=True)
    tinh_tp = models.TextField(blank=True, null=True)
    quan_huyen = models.TextField(blank=True, null=True)
    phuong_xa = models.TextField(blank=True, null=True)
    tt_phap_ly = models.TextField(blank=True, null=True)
    gia = models.TextField(blank=True, null=True)
    dien_tich = models.TextField(blank=True, null=True)
    mo_ta = models.TextField(blank=True, null=True)
    nguoi_dang = models.TextField(blank=True, null=True)
    sdt = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data2'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Nguoidang(models.Model):
    id_nguoidang = models.AutoField(primary_key=True)
    nguoi_dang = models.TextField(blank=True, null=True)
    sdt = models.TextField(blank=True, null=True)
    so_like = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nguoidang'


class Taikhoan(models.Model):
    ten = models.CharField(max_length=200)
    diachi = models.CharField(max_length=200)
    dienthoai = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    matkhau = models.CharField(max_length=100)
    solike = models.IntegerField()
    phanquyen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taikhoan'


class Tindaluu(models.Model):
    id_taikhoan = models.ForeignKey(Taikhoan, models.DO_NOTHING, db_column='id_taikhoan')
    id_baidang = models.ForeignKey(Data2, models.DO_NOTHING, db_column='id_baidang')

    class Meta:
        managed = False
        db_table = 'tindaluu'
