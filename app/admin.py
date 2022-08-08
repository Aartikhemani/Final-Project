from django.contrib import admin

from .models import Cart, Category, Customer, OrderPlaced, Product, Tag

# Register your models here.
# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Cart)
# admin.site.register(OrderPlaced)
admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "city", "zipcode", "state", "country"]


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "selling_price",
        "discounted_price",
        "description",
        "category",
        "product_image",
    ]


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "quantity"]


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "customer", "product", "ordered_date", "status"]
