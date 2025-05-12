from django.urls import path
from .views import *

urlpatterns = [
    path('', BookListApiView.as_view(), name='book_list'),
]
