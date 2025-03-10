# Generated by Django 4.2.7 on 2024-05-03 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=16, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('type', models.CharField(max_length=16, verbose_name='用户类型')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='emoSocialApp.user')),
                ('name', models.CharField(max_length=16, verbose_name='昵称')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('gender', models.CharField(max_length=16, verbose_name='性别')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('avatar', models.ImageField(null=True, upload_to='', verbose_name='头像')),
                ('signature', models.CharField(max_length=32, null=True, verbose_name='个性签名')),
            ],
        ),
    ]
