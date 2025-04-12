from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test


def book_list(request):
    books = Book.objects.all()
    per_page = request.GET.get("per_page", 5)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 5
    paginator = Paginator(books, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_obj': page_obj, "per_page": per_page})

@login_required
def book_create(request):
    if request.user.role in ['user', 'admin']:
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_list')
        else:
            form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@user_passes_test(lambda user: user.is_authenticated and user.role=='admin')
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.price = request.POST.get("price")
        book.save()
        return redirect("book_list")
    return render(request, "books/book_form.html", {"book": book})

@user_passes_test(lambda user: user.is_authenticated and user.role=='admin')
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

