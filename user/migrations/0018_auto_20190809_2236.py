# Generated by Django 2.2.4 on 2019-08-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('남성', '남성'), ('여성', '여성')], max_length=4, null=True, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('모델', '모델'), ('사진작가', '사진작가'), ('일반인', '일반인')], max_length=6, null=True, verbose_name='역할'),
        ),
    ]