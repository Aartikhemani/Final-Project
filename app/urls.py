from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from app import views

from .forms import *

urlpatterns = [
    # path('', views.home),
    path("", views.ProductView.as_view(), name="home"),
    path("search/", views.search, name="search"),
    path(
        "product-detail/<int:pk>",
        views.ProductDetailView.as_view(),
        name="product-detail",
    ),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.show_cart, name="show_cart"),
    path("buy/", views.buy_now, name="buy-now"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    path("retro-walk/", views.retro_walk, name="retro_walk"),
    path("retro-walk/<slug:data>", views.retro_walk, name="retro_data"),
    path("bold-daisy/", views.bold_daisy, name="bold_daisy"),
    path("bold-daisy/<slug:data>", views.bold_daisy, name="daisy_data"),
    path("top-wear/", views.top_wear, name="top_wear"),
    path("top-wear/<slug:data>", views.top_wear, name="top_data"),
    path("bottom-wear/", views.bottom_wear, name="bottom_wear"),
    path("bottom-wear/<slug:data>", views.bottom_wear, name="bottom_data"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="app/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path(
        "registration/",
        views.CustomerRegistrationView.as_view(),
        name="customer_registration",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="app/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="app/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="app/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="app/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("checkout/", views.checkout, name="checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
