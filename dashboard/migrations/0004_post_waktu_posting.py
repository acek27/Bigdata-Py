# Generated by Django 3.0.4 on 2020-03-13 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_post_alamat'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='waktu_posting',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]