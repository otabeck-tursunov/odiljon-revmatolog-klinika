# Generated by Django 4.2.1 on 2023-09-05 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bemor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familiya', models.CharField(max_length=100)),
                ('sharif', models.CharField(max_length=100)),
                ('tugilgan_sana', models.DateField(blank=True, null=True)),
                ('tel', models.CharField(max_length=15)),
                ('manzil', models.CharField(max_length=150)),
                ('balans', models.IntegerField(default=0)),
                ('royhatdan_otgan_sana', models.DateField(auto_now_add=True, null=True)),
                ('joylashgan', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['familiya', 'ism'],
            },
        ),
        migrations.CreateModel(
            name='Joylashtirish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelish_sanasi', models.DateField()),
                ('ketish_sanasi', models.DateField(blank=True, null=True)),
                ('kelish_vaqti', models.TimeField(blank=True, null=True)),
                ('ketish_vaqti', models.TimeField(blank=True, null=True)),
                ('qarovchi', models.BooleanField(default=False)),
                ('yotgan_kun_soni', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('bemor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.bemor')),
            ],
        ),
        migrations.CreateModel(
            name='SubYollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('matn', models.TextField()),
                ('narx', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tolov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.PositiveBigIntegerField()),
                ('tolangan_summa', models.JSONField(blank=True, default=[], null=True)),
                ('sana', models.DateField(auto_now_add=True)),
                ('turi', models.CharField(blank=True, choices=[('Naqd', 'Naqd'), ('Plastik', 'Plastik')], max_length=50)),
                ('tolandi', models.BooleanField(default=False)),
                ('xulosa_holati', models.CharField(blank=True, choices=[('Topshirilyapti', 'Topshirilyapti'), ('Kutyapti', 'Kutyapti'), ('Kiritildi', 'Kiritildi')], max_length=30, null=True)),
                ('tolangan_sana', models.DateField(blank=True, null=True)),
                ('ozgartirilgan_sana', models.DateField(blank=True, null=True)),
                ('haqdor', models.BooleanField(default=False)),
                ('tolov_qaytarildi', models.BooleanField(default=False)),
                ('izoh', models.CharField(blank=True, max_length=300, null=True)),
                ('bemor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.bemor')),
                ('joylashtirish_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='register.joylashtirish')),
                ('subyollanma_idlar', models.ManyToManyField(to='register.subyollanma')),
            ],
        ),
        migrations.CreateModel(
            name='Xona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qavat', models.PositiveSmallIntegerField()),
                ('raqami', models.PositiveSmallIntegerField()),
                ('xona_sigimi', models.PositiveSmallIntegerField()),
                ('bosh_joy_soni', models.PositiveSmallIntegerField()),
                ('turi', models.CharField(choices=[('Lux', 'Lux'), ('Odatiy', 'Odatiy'), ('Pol-lux', 'Pol-lux')], max_length=20)),
                ('joy_narxi', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Yollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300)),
                ('header_text', models.TextField(blank=True, null=True)),
                ('footer_text', models.TextField(blank=True, null=True)),
                ('qayerga', models.CharField(max_length=50)),
                ('narx', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Xulosa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xulosa_matni', models.TextField()),
                ('sana', models.DateField(auto_now_add=True)),
                ('chop_etildi', models.BooleanField(default=False)),
                ('tolov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.tolov')),
            ],
        ),
        migrations.CreateModel(
            name='TolovQaytarish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.IntegerField()),
                ('sana', models.DateField(auto_now_add=True)),
                ('izoh', models.CharField(max_length=300)),
                ('tolov_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.tolov')),
            ],
        ),
        migrations.AddField(
            model_name='tolov',
            name='yollanma_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='register.yollanma'),
        ),
        migrations.AddField(
            model_name='subyollanma',
            name='yollanma_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.yollanma'),
        ),
        migrations.AddField(
            model_name='joylashtirish',
            name='xona_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.xona'),
        ),
        migrations.CreateModel(
            name='Chek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField()),
                ('vaqt', models.TimeField(blank=True, null=True)),
                ('tolov_maqsadlar', models.JSONField(default=[])),
                ('bemor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.bemor')),
                ('tolov_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='register.tolov')),
            ],
        ),
    ]