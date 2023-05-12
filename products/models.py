from django.db import models

# Create your models here.
# создание моделей=таблиц для баз данных
# модель с категорией товаров
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# модель с продуктами
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE) # тут параметр on_delete=PROTECT означает что невозможно будет удалить категорию товара, пока все продукты в этой категории не удаляться или не присвоится другая категория

    def __str__(self):
        return self.name