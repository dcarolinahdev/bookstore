# Python
import datetime
# Django
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Editorial(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    classification = models.TextChoices('fantasy', 'classic')
    numrpdb = models.IntegerField(default=0)
    summary = models.TextField(max_length=400)
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE)
    authors = models.ManyToManyField(
        Author, through='Creations', through_fields=('book', 'author'))

    def __str__(self):
        return self.title


class Creations(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    score = models.IntegerField(default=10)

    def __str__(self):
        return (self.book, '-', self.author)
