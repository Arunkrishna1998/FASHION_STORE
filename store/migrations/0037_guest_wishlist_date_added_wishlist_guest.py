# Generated by Django 4.2.3 on 2023-07-28 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_shippingaddress_is_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_id', models.CharField(blank=True, max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='wishlist',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.guest'),
        ),
    ]