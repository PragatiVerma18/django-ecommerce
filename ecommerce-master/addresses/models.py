from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    phone           = models.CharField(max_length=120, default="")
    address         = models.CharField(max_length=120)
    city            = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='India')
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{address}\n{city}\n{state}, {postal}\n{country}".format(
                address = self.address,
                city = self.city,
                state = self.state,
                postal= self.postal_code,
                country = self.country
            )
