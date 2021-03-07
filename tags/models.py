from django.db import models
from products.models import Product
from django.utils.text import slugify
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug  = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)