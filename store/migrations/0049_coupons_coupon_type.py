# Generated by Django 4.2.3 on 2023-08-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0048_coupon_redeemed_details_is_redeemed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='coupon_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
