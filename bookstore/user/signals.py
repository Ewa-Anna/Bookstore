from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import ShippingAddress


# when user chooses main address field to be True, all other shipping addresses will switch to False
@receiver(pre_save, sender=ShippingAddress)
def set_main_address(sender, instance, **kwargs):
    if instance.main:
        ShippingAddress.objects.filter(user=instance.user).exclude(
            id=instance.id
        ).update(main=False)
