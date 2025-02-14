from inventory.models import Product, InventoryLog

# Fetch a product
product = Product.objects.first()

# Create a test log
log = InventoryLog.objects.create(
    product=product,
    change_type='removed',
    quantity_changed=2
)

# Check if it's saved
print(InventoryLog.objects.all())
