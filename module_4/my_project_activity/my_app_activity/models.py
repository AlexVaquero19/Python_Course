from django.db import models 
from django.utils import timezone

class Author(models.Model): 
    name = models.CharField(max_length=100) 
    email = models.EmailField() 
    date_of_birth = models.DateField() 

    def __str__(self): 
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date_of_posted = models.DateField(default=timezone.now)

class User(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date_of_creation = models.DateField(default=timezone.now)
