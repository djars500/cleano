# Generated by Django 3.2 on 2021-09-05 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_zayavka_house'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courier',
            options={'verbose_name': 'Курьера', 'verbose_name_plural': 'Курьеры'},
        ),
        migrations.RemoveField(
            model_name='courier',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='courier',
            name='name',
        ),
        migrations.RemoveField(
            model_name='courier',
            name='password',
        ),
        migrations.RemoveField(
            model_name='courier',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='courier',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='courier',
            name='username',
        ),
        migrations.AddField(
            model_name='courier',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]