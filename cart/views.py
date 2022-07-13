from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from products.models import Album
from django.utils import timezone

# Create your views here.



def add_to_cart(request, slug):
    item = get_object_or_404(Album, slug=slug)
    order_item = OrderItem.objects.get_or_create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()

        else:

            order_items.add(order_item)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)

        return redirect('album', slug=slug)


    return redirect('album', slug=slug) 
