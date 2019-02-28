from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.book, name="book"),
    url(r'books/(?P<id>\d+)/$', views.show, name="show"),
    url(r'^books/add/$', views.add, name="add"),
    url(r'^books/add_book_to_db/$', views.add_book_to_db, name="add_book_to_db"),
    url(r'^books/add_review/(?P<id>\d+)/$',
        views.add_review, name="add_review"),
    url(r'^users/(?P<id>\d+)/$', views.user, name='user'),
    url(r'^users/delete/(?P<id>\d+)/$', views.delete, name="delete"),
    url(r'^review/destroy/$', views.destroy, name="destroy")
]
