# Generated by Django 5.0.1 on 2024-01-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='obtainTime',
            field=models.CharField(choices=[('Jan', 'January'), ('Feb', 'Feburary'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], default='Jan', max_length=3),
        ),
    ]