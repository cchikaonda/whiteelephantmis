# Generated by Django 4.1.7 on 2023-03-29 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0006_remove_requisition_requested'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisition',
            options={'ordering': ['code'], 'permissions': [('can_approve_requisition', 'can approve requisition'), ('can_view_all_requisitions', 'can view all requsitions')]},
        ),
    ]
