# Generated by Django 5.0.1 on 2024-01-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0004_alter_seed_plantimg_alter_seed_seedimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='img',
            field=models.ImageField(default='default_seed_pic.PNG', upload_to='step_pics'),
        ),
    ]
