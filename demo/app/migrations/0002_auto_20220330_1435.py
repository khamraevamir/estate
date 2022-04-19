# Generated by Django 3.2.6 on 2022-03-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='building_type',
            field=models.CharField(choices=[('Variant1', 'Variant2')], max_length=300, null=True, verbose_name='Тип строения'),
        ),
        migrations.AddField(
            model_name='flat',
            name='repaoir',
            field=models.CharField(choices=[('Variant1', 'Variant2')], max_length=300, null=True, verbose_name='Ремонт'),
        ),
    ]
