from django.shortcuts import render, redirect
from .models import Book, Review
from django.contrib import messages
from ..login.models import User

# Create your views here.


def book(request):
    context = {
        'logged_user': User.objects.get(id=request.session['user_id']),
        'latest_reviews': Review.objects.filter(reviewing_user=request.session['user_id']).order_by('-created_at')[:3],
        'all_books': Book.objects.all()
    }
    return render(request, 'books/book.html', context)


def show(request, id):
    context = {
        'login_user': User.objects.get(id=request.session['user_id']),
        'book': Book.objects.get(id=id),
        'reviews': Review.objects.filter(reviewing_book=id).order_by('-created_at'),
    }
    return render(request, 'books/view_book.html', context)


def add(request):
    return render(request, 'books/addBooks.html')


def add_book_to_db(request):
    this_user = User.objects.get(id=request.session['user_id'])
    errors = Book.objects.validate(request.POST)

    if len(request.POST['add_author']) < 1:
        added_author = request.POST['select_author']
    else:
        added_author = request.POST['add_author']

    if request.POST:
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('books:add')
        this_book = Book.objects.create(
            title=request.POST['title'], author=added_author, submitted_user=this_user)
        Review.objects.create(
            review=request.POST['review'], rating=request.POST['ratings'], reviewing_book=this_book, reviewing_user=this_user)
        return redirect('books:show', id=this_book.id)


def add_review(request, id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=id)
    errors = Review.objects.validate(request.POST)
    if request.POST:
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('books:show', id=id)
        Review.objects.create(
            review=request.POST['review'], rating=request.POST['ratings'], reviewing_book=this_book, reviewing_user=this_user)
        return redirect('books:show', id=id)


def user(request, id):
    if 'user_id' not in request.session:
        return redirect('login:index')
    context = {
        'user': User.objects.get(id=id),
        'all_reviews': Review.objects.filter(reviewing_user=id),
        'total_review': Review.objects.filter(reviewing_user=id).count()
    }
    return render(request, 'books/user.html', context)


def delete(request, id):
    context = {
        'review': Review.objects.get(id=id)
    }
    return render(request, 'books/message.html', context)


def destroy(request):
    Review.objects.get(id=request.POST['id']).delete()
    return redirect('books:book')
