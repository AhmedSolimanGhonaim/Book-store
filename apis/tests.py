from django.test import TestCase

# Create your tests here.
from books.models import Book
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse




class APITEST(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2023-01-01',
            isbn='1234567890123',
            pages=100,
            cover_image='http://example.com/image.jpg',
            language='English'
        )
    def test_api_listview(self):
            response = self.client.get(reverse('book_list'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(Book.objects.count(), 1)
            self.assertContains(response,self.book.title)