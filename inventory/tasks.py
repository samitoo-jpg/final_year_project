def check_inventory_levels():
    low_stock_products = Product.objects.filter(stock_quantity__lte=models.F('reorder_threshold'))
    if low_stock_products.exists():
        message = "The following products need restocking:\n" + "\n".join([p.name for p in low_stock_products])
        send_mail(
            'Inventory Alert',
            message,
            'admin@inventory.com',
            ['manager@store.com'],
            fail_silently=False,
        )