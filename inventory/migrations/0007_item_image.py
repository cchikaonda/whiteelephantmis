# Generated by Django 4.1.7 on 2023-03-20 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_batchnumber_options_alter_unit_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='ecom_product6_b.png', null=True, upload_to='items/'),
        ),
    ]
