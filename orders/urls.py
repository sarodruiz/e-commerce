from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("menu/", views.menu, name="menu"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("remove-from-cart/", views.remove_from_cart, name="remove-from-cart"),
    path("cart/", views.cart, name="cart"),
    path("create-checkout-session", views.create_checkout_session, name="create-checkout-session"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel")
]