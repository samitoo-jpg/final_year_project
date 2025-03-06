import csv
import os
from django.core.management.base import BaseCommand
from inventory.models import Product, Category, Supplier

class Command(BaseCommand):
    help = "Import inventory data from retail_store_inventory.csv"

    def handle(self, *args, **kwargs):
        file_path = os.path.abspath("retail_store_inventory.csv")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR("CSV file not found! Make sure it's in the project root."))
            return

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                category, _ = Category.objects.get_or_create(name=row["Category"])
                supplier, _ = Supplier.objects.get_or_create(name=row["Store ID"])

                Product.objects.update_or_create(
                    name=row["Product ID"],  # Use Product ID as the name (fix for error)
                    defaults={
                        "category": category,
                        "supplier": supplier,
                        "stock_quantity": int(row["Inventory Level"]),
                        "price": float(row["Price"]),
                        "reorder_threshold": int(row["Units Ordered"]),
                    }
                )

        self.stdout.write(self.style.SUCCESS("✅ Inventory data imported successfully!"))


