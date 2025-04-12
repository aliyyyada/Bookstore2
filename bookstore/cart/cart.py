from books.models import Book

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart']={}
        self.cart = cart

    def add(self, book, quantity = 1):
        book_id = str(book.id)
        if book_id in self.cart:
            self.cart[book_id]['quantity']+=quantity
        else:
            self.cart[book_id] = {'quantity': quantity}
        self.save()

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session['cart']={}
        self.save()

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in = book_ids)
        for book in books:
            book_id = str(book.id)
            self.cart[book_id]['book']=book
            self.cart[book_id]['total_price']=book.price * self.cart[book_id]['quantity']
            yield self.cart[book_id]

    def get_total_price(self):
        return sum(item['book'].price * item['quantity'] for item in self)