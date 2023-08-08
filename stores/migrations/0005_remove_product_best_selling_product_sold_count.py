# Generated by Django 4.2.3 on 2023-07-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_product_best_selling_product_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Best_selling',
        ),
        migrations.AddField(
            model_name='product',
            name='sold_count',
            field=models.IntegerField(default=0),
        ),
    ]
