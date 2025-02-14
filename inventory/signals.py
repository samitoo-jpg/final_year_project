from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, OrderItem, InventoryLog, Product

@receiver(post_save, sender=OrderItem)
def update_stock_on_order(sender, instance, created, **kwargs):
    """Updates stock when an order is placed or received"""
    if created:
        order = instance.order
        product = instance.product

        if order.order_type == 'out':  # Stock Out
            product.quantity -= instance.quantity
            change_type = 'removed'
        else:  # Stock In
            product.quantity += instance.quantity
            change_type = 'added'

        product.save()

        # Create an inventory log entry
        InventoryLog.objects.create(
            product=product,
            change_type=change_type,
            quantity_changed=instance.quantity
        )
