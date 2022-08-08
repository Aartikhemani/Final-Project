from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import CustomerProfileForm, CustomerRegistrationForm
from .models import *


class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category__title__contains="Top Wear")
        bottomwears = Product.objects.filter(category__title__contains="Bottom Wear")
        return render(
            request, "app/home.html", {"topwears": topwears, "bottomwears": bottomwears}
        )


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/product_detail.html", {"product": product})


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get("product_id")
    product = Product.objects.get(id=product_id)
    cart = Cart(user=user, product=product)
    cart.save()
    return redirect("/cart")


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        total_amount = 0.0
        cart_product = []
        for product in Cart.objects.all():
            if product.user == user:
                cart_product.append(product)
        if cart_product:
            for product in cart_product:
                product_amount = product.quantity * product.product.selling_price
                total_amount += product_amount
        return render(
            request,
            "app/add_to_cart.html",
            {"cart": cart, "total_amount": total_amount},
        )


def buy_now(request):
    return render(request, "app/buy_now.html")


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(
            request, "app/profile.html", {"form": form, "active": "btn-primary"}
        )

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            city = form.cleaned_data["city"]
            zipcode = form.cleaned_data["zipcode"]
            state = form.cleaned_data["state"]
            country = form.cleaned_data["country"]
            register = Customer(
                user=user,
                name=name,
                city=city,
                zipcode=zipcode,
                state=state,
                country=country,
            )
            register.save()
            messages.success(request, "Profile Updated")
        return render(
            request, "app/profile.html", {"form": form, "active": "btn-primary"}
        )


def address(request):
    customer_address = Customer.objects.filter(user=request.user)
    return render(
        request,
        "app/address.html",
        {"customer_address": customer_address, "active": "btn-primary"},
    )


def orders(request):
    return render(request, "app/orders.html")


def retro_walk(request, data=None):
    if data == None:
        retro = Product.objects.filter(category__title__contains="Retro Walk")
    elif data == "low":
        retro = Product.objects.filter(category__title__contains="Retro Walk").order_by(
            "selling_price"
        )
    elif data == "h2l":
        retro = Product.objects.filter(category__title__contains="Retro Walk").order_by(
            "-selling_price"
        )
    return render(request, "app/retro.html", {"retro": retro})


def bold_daisy(request, data=None):
    if data == None:
        daisy = Product.objects.filter(category__title__contains="Bold Daisy")
    elif data == "low":
        daisy = Product.objects.filter(category__title__contains="Bold Daisy").order_by(
            "selling_price"
        )
    elif data == "h2l":
        daisy = Product.objects.filter(category__title__contains="Bold Daisy").order_by(
            "-selling_price"
        )
    return render(request, "app/daisy.html", {"daisy": daisy})


def top_wear(request, data=None):
    if data is None:
        top = Product.objects.filter(category__title__contains="Top Wear")
    elif data == "low":
        top = Product.objects.filter(category__title__contains="Top Wear").order_by(
            "selling_price"
        )
    elif data == "h2l":
        top = Product.objects.filter(category__title__contains="Top Wear").order_by(
            "-selling_price"
        )
    return render(request, "app/top_wear.html", {"top": top})


def bottom_wear(request, data=None):
    if data is None:
        bottom = Product.objects.filter(category__title__contains="Bottom Wear")
    elif data == "low":
        bottom = Product.objects.filter(
            category__title__contains="Bottom Wear"
        ).order_by("selling_price")
    elif data == "h2l":
        bottom = Product.objects.filter(
            category__title__contains="Bottom Wear"
        ).order_by("-selling_price")
    return render(request, "app/bottom_wear.html", {"bottom": bottom})


def login(request):
    return render(request, "app/login.html")


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app/customer_registration.html", {"form": form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulation! registered successfully")
            form.save()
        return render(request, "app/customer_registration.html", {"form": form})


def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_item = Cart.objects.filter(user=user)
    total_amount = 0.0
    cart_product = []
    for product in Cart.objects.all():
        if product.user == user:
            cart_product.append(product)
    if cart_product:
        for product in cart_product:
            product_amount = product.quantity * product.product.selling_price
            total_amount += product_amount

    return render(
        request,
        "app/checkout.html",
        {"add": add, "cart_item": cart_item, "total_amount": total_amount},
    )


# [p for p in Cart.objects.all() if p.user == user]


def search(request):
    query = request.GET["query"]
    products = Product.objects.filter(
        Q(title__icontains=query) | Q(tags__title__icontains=query)
    )
    return render(request, "app/search.html", {"products": products})
