import random
import os
from django.db import models
from django.utils.text import slugify
from .generator import random_string_generator, unique_slug_generator
from django.db.models.signals import pre_save



# Create your models here.






def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 378937839)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductManager(models.Manager):
    def get_by_slug(self, product_slug):
        qs = self.get_queryset().filter(slug=product_slug)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)
    image = models.ImageField(upload_to='upload_image_path', null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()

    # def save(self, *args, **kwargs):
    #     if not self.slug and self.title:
    #         self.slug = slugify(self.title)
    #     super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
