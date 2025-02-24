from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_useractivitylog'),  # Change to the last migration file
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalStock',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('product_id', models.IntegerField()),
                ('stock_level', models.IntegerField()),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AIStockForecast',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('product_id', models.IntegerField()),
                ('predicted_stock', models.IntegerField()),
                ('prediction_date', models.DateField()),
                ('confidence_level', models.DecimalField(max_digits=5, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
