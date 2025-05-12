from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Book


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book=Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2023-01-01',
            isbn='1234567890123',
            pages=100,
            cover_image='http://example.com/image.jpg',
            language='English'
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.published_date, '2023-01-01')
        self.assertEqual(self.book.isbn, '1234567890123')
        self.assertEqual(self.book.pages, 100)
        self.assertEqual(self.book.cover_image, 'http://example.com/image.jpg')
        self.assertEqual(self.book.language, 'English')
    
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")   