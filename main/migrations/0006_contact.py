# Generated by Django 3.2 on 2021-09-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_zayavka_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Контактные данные',
                'verbose_name_plural': 'Контактные данные',
            },
        ),
    ]
