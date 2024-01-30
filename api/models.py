from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.CharField(max_length=20)
    product_name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    discounted_price=models.CharField(max_length=20)
    actual_price=models.CharField(max_length=20)
    discount_percentage=models.CharField(max_length=20)
    rating=models.FloatField()
    rating_count=models.CharField(max_length=25)
    about_product=models.TextField()
    user_id=models.CharField(max_length=255)
    user_name=models.CharField(max_length=255)
    review_id=models.CharField(max_length=255)
    review_title=models.CharField(max_length=255)
    review_content=models.TextField()
    img_link=models.URLField()
    product_link=models.URLField()
