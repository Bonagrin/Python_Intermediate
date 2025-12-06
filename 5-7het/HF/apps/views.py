from django.shortcuts import render, redirect
from django.urls import reverse
from konyv_app.models import Author, Book


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "admin":
            return redirect('home')
        else:
            return render(request, "login.html", {
                "error": "Hibás felhasználónév vagy jelszó!"
            })

    return render(request, "login.html")


def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    isbn = Book.objects.all()
    return render(request, 'home.html', {
        'authors': authors,
        'books': books,
        'isbn': isbn,
    })


def add_author(request):
    return render(request, 'author.html')


def add_author_record(request):
    Author.objects.create(
        name=request.POST.get('name')
    )
    return redirect('home')


def update_author(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'author.html', {'author': author})


def update_author_record(request, id):
    author = Author.objects.get(id=id)
    author.name = request.POST.get('name')
    author.save()
    return redirect('home')


def delete_author(request, id):
    Author.objects.get(id=id).delete()
    return redirect('home')


def add_book(request):
    authors_qs = Author.objects.all()
    return render(request, 'book.html', {
        'authors': authors_qs,
        'no_authors': not authors_qs.exists(),
    })


def add_book_record(request):
    if not Author.objects.exists():
        return redirect('home')

    author_id = request.POST.get('author_id')
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return redirect('home')

    Book.objects.create(
        name=request.POST.get('name'),
        isbn=request.POST.get('isbn'),
        author=author
    )
    return redirect('home')


def update_book(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book.html', {
        'book': book,
        'authors': Author.objects.all(),
    })


def update_book_record(request, id):
    book = Book.objects.get(id=id)
    book.name = request.POST.get('name')
    book.isbn = request.POST.get('isbn')
    book.author = Author.objects.get(id=request.POST.get('author_id'))
    book.save()
    return redirect('home')


def delete_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect('home')
