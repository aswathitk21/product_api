# Generated by Django 4.2.9 on 2024-01-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.FloatField()),
                ('rating_count', models.FloatField()),
                ('about_product', models.TextField()),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=255)),
                ('review_id', models.IntegerField()),
                ('review_title', models.CharField(max_length=255)),
                ('review_content', models.TextField()),
                ('img_link', models.URLField()),
                ('product_link', models.URLField()),
            ],
        ),
    ]
