from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

#
# CATEGORY_CHOICE = (
#     ('Retro Walk', 'Retro Walk'),
#     ('Bold Daisy', 'Bold Daisy'),
#     ('Top Wear', 'Top Wear'),
#     ('Bottom Wear', 'Bottom Wear'))


class Tags(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField(null=True,blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    product_image = models.ImageField(upload_to='productImages',default=False)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Cart"

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


STATUS_CHOICES = (
    ('Pending','Pending'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        verbose_name_plural = "Order placed"