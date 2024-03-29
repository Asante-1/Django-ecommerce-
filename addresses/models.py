from django.db import models
from billing.models import BillingProfile

# Create your models here.


class Address(models.Model):
    ADDEESS_TYPES = (
        ('billing', 'BILLING'),
        ('shipping', 'SHIPPING'),

    )


    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=120, choices=ADDEESS_TYPES)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default='Canada')
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)