from django.db import models
from ..login.models import User

# Create your models here.


class BookManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData['title']) < 5:
            errors.append("Book title must be at least 5 letters long.")
        if len(postData['review']) < 5:
            errors.append("Review must be at least 5 letters long.")
        elif len(postData['review']) > 300:
            errors.apend("Review must be less than 300 letters long.")
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_user = models.ForeignKey(User, related_name="books")

    def __str__(self):
        return self.title
    objects = BookManager()


class ReviewManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData['review']) < 5:
            errors.append("This field must be at least 5 letters long.")
        elif len(postData['review']) > 300:
            errors.apend("This field must be less than 300 letters long.")
        return errors


class Review(models.Model):
    review = models.CharField(max_length=255)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewing_book = models.ForeignKey(Book, related_name="book_reviews")
    reviewing_user = models.ForeignKey(User, related_name="user_reviews")

    objects = ReviewManager()
