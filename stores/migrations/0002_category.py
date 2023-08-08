# Generated by Django 4.2.3 on 2023-07-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('image', models.ImageField(null=True, upload_to='category')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
