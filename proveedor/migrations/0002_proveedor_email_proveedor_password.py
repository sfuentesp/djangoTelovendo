# Generated by Django 4.0.2 on 2022-02-05 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='password',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
    ]