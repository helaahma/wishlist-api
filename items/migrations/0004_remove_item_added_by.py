# Generated by Django 2.2.3 on 2019-07-31 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='added_by',
        ),
    ]