# Generated by Django 4.2.4 on 2023-09-02 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='file',
            field=models.FileField(upload_to='newapp/static'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='file',
            field=models.FileField(upload_to='newapp/static'),
        ),
    ]