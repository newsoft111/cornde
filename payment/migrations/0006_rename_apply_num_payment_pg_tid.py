# Generated by Django 4.0.4 on 2022-04-25 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_payment_referral'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='apply_num',
            new_name='pg_tid',
        ),
    ]
