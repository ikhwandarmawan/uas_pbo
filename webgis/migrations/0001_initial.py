# Generated by Django 4.1.1 on 2023-01-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetaBanjir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('garis_lintang', models.IntegerField()),
                ('garis_bujur', models.IntegerField()),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
                ('ketinggian', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]