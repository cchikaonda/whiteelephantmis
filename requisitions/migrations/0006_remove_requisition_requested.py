# Generated by Django 4.1.7 on 2023-03-23 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0005_requisition_approved_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='requested',
        ),
    ]