# Generated by Django 4.2.11 on 2024-05-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolhub', '0009_alter_ordereditem_owner_alter_ordereditem_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='ordereditem',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='ordereditem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderedItem',
        ),
    ]