# Generated by Django 4.2.3 on 2023-08-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_coupon_redeemed_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon_redeemed_details',
            name='is_redeemed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coupon_redeemed_details',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]