from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Cart, CartItem, Order, Product
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

@method_decorator(cache_page(60), name='get')
class CartView(generic.TemplateView):
    template_name = "basket/cart_view.html"

    def get_context_data(self, **kwargs):
        return {"cart": Cart.objects.get_or_create(user=self.request.user)[0]}


class UpdateCartView(generic.UpdateView):
    model = Cart
    def post(self, request, product_id, quantity):
        cart_item = get_object_or_404(CartItem, cart__user=request.user, product_id=product_id)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        messages.success(request, 'Корзина обновлена')
        cache.clear()
        return redirect('cart_view')

class RemoveFromCartView(generic.DeleteView):
    def post(self, request, product_id):
        get_object_or_404(CartItem, cart__user=request.user, product_id=product_id).delete()
        messages.success(request, 'Товар удален из корзины')
        cache.clear()
        return redirect('cart_view')

@method_decorator(cache_page(60), name='get')
class CheckoutView(generic.TemplateView):
    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        if not cart.items.exists():
            messages.error(request, 'Корзина пуста!')
            return redirect('cart_view')

        Order.objects.create(
            cart=cart, user=request.user, address_line_1='Введите адрес',
            phone_number='Введите номер', total_price=cart.total_price()
        )
        cart.items.all().delete()
        messages.success(request, 'Заказ оформлен!')
        cache.clear()
        return redirect('cart_view')
