# Generated by Django 5.0.1 on 2024-02-23 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0010_alter_seed_obtaintime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='growthRate',
            field=models.CharField(choices=[('slow', 'slow'), ('medium', 'medium'), ('Fast', 'Fast'), ('Depends on their mood', 'Depends on their mood')], default='Depends on their mood', max_length=30),
        ),
    ]