# Generated by Django 4.1.1 on 2023-01-02 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgis', '0004_alter_petabanjir_garis_bujur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='petabanjir',
            name='wilayah',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
