from django.urls import path
from .views import HomeView
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('booklist/', BookListView.as_view(), name='booklist'),
    path('booklist/<int:id>', BookDetailView.as_view(), name='bookdetail'),
]