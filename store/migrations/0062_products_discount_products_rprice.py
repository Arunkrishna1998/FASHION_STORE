# Generated by Django 4.2.3 on 2023-08-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0061_alter_orderproduct_order_alter_orderproduct_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='rprice',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]