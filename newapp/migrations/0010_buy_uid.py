# Generated by Django 4.2.4 on 2023-09-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_remove_buy_option1_remove_buy_option2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
