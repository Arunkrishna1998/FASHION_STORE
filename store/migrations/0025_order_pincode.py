# Generated by Django 4.2.3 on 2023-07-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_orderproduct_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
