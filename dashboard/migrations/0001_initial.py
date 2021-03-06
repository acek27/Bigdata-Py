# Generated by Django 3.0.4 on 2020-03-17 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('jenis_kelamin', models.SmallIntegerField()),
                ('tempat_lahir', models.CharField(max_length=255)),
                ('tanggal_lahir', models.DateField()),
                ('email', models.EmailField(default='email@gmail.com', max_length=254)),
                ('alamat', models.CharField(default='Situbondo', max_length=200)),
                ('hp', models.CharField(max_length=13)),
                ('timestaps', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
