# Generated by Django 3.2 on 2021-09-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210917_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='zayavka',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]