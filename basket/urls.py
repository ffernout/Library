from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.CartView.as_view(), name='add_to_cart'),
    path('cart/', views.CartView, name='cart_view'),
    path('update_cart/<int:product_id>/<int:quantity>/', views.UpdateCartView.as_view(), name='update_cart'),
    path('remove_from_cart/<int:product_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
]