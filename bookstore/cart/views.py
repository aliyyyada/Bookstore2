from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from .cart import Cart

def cart_view(request):
    cart= Cart(request)
    return render(request, 'cart/cart.html', {'cart':cart, 'total':cart.get_total_price()})

def add_to_cart(request, book_id):
    cart = Cart(request)
    book =get_object_or_404(Book, id=book_id)
    cart.add(book)
    return redirect('book_list')

def remove_from_cart(request, book_id):
    cart=Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart_view')

