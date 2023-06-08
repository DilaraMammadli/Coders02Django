from django.db import models
from .validators import validate_timestamp
from ckeditor.fields import RichTextField


class Product(models.Model):
    name = models.CharField(max_length=300)
    content = RichTextField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True, validators=[validate_timestamp])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name