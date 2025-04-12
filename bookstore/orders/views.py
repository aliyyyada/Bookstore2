from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrederItem
from books.models import Book

@login_required
def my_orders(request):
    orders = Order.objects.filter(user= request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required
def place_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')

    total = 0
    items =[]
    for book_id, item in cart.items():
        quantity = item['quantity']
        book = Book.objects.get(id=book_id)
        items.append((book, quantity, book.price))

    order = Order.objects.create(user=request.user)
    for book, quantity, price in items:
        OrederItem.objects.create(order = order, book = book, quantity = quantity)

    request.session['cart']={}
    return redirect('my_orders')