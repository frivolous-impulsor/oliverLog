# Generated by Django 5.0.1 on 2024-02-06 22:05

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0007_alter_seed_seedname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='plantImg',
            field=django_resized.forms.ResizedImageField(crop=None, default='default_plant_pic.PNG', force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 300], upload_to='plant_pics'),
        ),
        migrations.AlterField(
            model_name='seed',
            name='seedImg',
            field=django_resized.forms.ResizedImageField(crop=None, default='default_seed_pic.PNG', force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 300], upload_to='seed_pics'),
        ),
    ]