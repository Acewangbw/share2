# Generated by Django 2.0 on 2019-02-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_userprofile_models_introdoction'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='site',
            field=models.CharField(default=1, max_length=32, unique=True, verbose_name='主页'),
            preserve_default=False,
        ),
    ]
