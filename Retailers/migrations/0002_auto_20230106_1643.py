# Generated by Django 3.2.9 on 2023-01-06 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Retailers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ManyToManyField(to='Retailers.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='retailer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Retailers.retailer'),
            preserve_default=False,
        ),
    ]