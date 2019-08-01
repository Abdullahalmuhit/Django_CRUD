from django.shortcuts import render, redirect
from .models import BookList

def index(request):
    books = BookList.objects.all()
    return render(request,'index.html', {'books':books})

def edit(request, id):
    books = BookList.objects.get(pk=id)
    return render(request, 'edit.html', {'books':books})


def update(request, id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect("/")

def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')

def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = BookList(title=title, price=price, author=author)
    book_details.save()
    return redirect('/')

def add_book(request):
    return render(request, 'add_book.html')

