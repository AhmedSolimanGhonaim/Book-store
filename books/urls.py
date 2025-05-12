from .views import *
from django.urls import path

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
]
