# Generated by Django 4.1.7 on 2024-06-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profi_main', '0002_alter_product_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='time_prog',
        ),
        migrations.AddField(
            model_name='product',
            name='description2',
            field=models.TextField(blank=True),
        ),
    ]