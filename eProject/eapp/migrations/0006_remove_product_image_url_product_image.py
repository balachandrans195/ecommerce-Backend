# Generated by Django 5.0.2 on 2024-03-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0005_alter_customer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
