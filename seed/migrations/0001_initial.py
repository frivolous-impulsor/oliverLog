# Generated by Django 5.0.1 on 2024-01-25 21:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('seedName', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('seedImg', models.ImageField(upload_to=None)),
                ('obtainTime', models.CharField(choices=[('Jan', 'January'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='Jan', max_length=3)),
                ('plantImg', models.ImageField(default='default.jpg', upload_to=None)),
                ('growthRate', models.IntegerField(default=0)),
                ('edibleFruit', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='default.jpg', upload_to=None)),
                ('content', models.TextField()),
                ('seed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.seed')),
            ],
        ),
    ]
