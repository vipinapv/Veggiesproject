# Generated by Django 4.2.4 on 2023-09-02 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('productid', models.CharField(max_length=10)),
                ('productname', models.CharField(max_length=50)),
                ('productdescription', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('file', models.FileField(upload_to='mainapp/static')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50)),
                ('productid', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('file', models.FileField(upload_to='mainapp/static')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
            ],
        ),
    ]