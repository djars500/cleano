# Generated by Django 3.2 on 2021-09-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_courier_in_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='statuc',
            field=models.CharField(blank=True, choices=[('В ожидании', 'В ожидании'), ('На отработке', 'На отработке'), ('Заказ выполнен', 'Заказ выполнен')], default='В ожидании', max_length=255, null=True, verbose_name='Статус заявки'),
        ),
    ]
