from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover_image = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=30)


    def __str__(self):
        return f"{self.title} by {self.author}"
