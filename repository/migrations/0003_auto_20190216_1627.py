# Generated by Django 2.0 on 2019-02-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20190211_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/avatar', verbose_name='头像'),
        ),
    ]
