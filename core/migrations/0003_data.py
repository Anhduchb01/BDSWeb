# Generated by Django 3.2.13 on 2022-06-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id_baidang', models.IntegerField(primary_key=True, serialize=False)),
                ('nhu_cau', models.TextField(blank=True, null=True)),
                ('chuyen_muc', models.TextField(blank=True, null=True)),
                ('tinh_tp', models.TextField(blank=True, null=True)),
                ('quan_huyen', models.TextField(blank=True, null=True)),
                ('phuong_xa', models.TextField(blank=True, null=True)),
                ('tt_phap_ly', models.TextField(blank=True, null=True)),
                ('gia', models.TextField(blank=True, null=True)),
                ('gia_tien', models.FloatField(blank=True, null=True)),
                ('donvi_gia', models.TextField(blank=True, null=True)),
                ('dien_tich', models.TextField(blank=True, null=True)),
                ('dien_tich1', models.FloatField()),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('id_nguoidang', models.IntegerField()),
                ('img', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'data',
                'managed': False,
            },
        ),
    ]
