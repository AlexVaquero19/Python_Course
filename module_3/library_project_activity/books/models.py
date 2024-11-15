from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    summary = models.CharField(max_length=255, blank=True)

    #If we print the Object Book, it is used to Print the Title Directly to not print the Object
    def __str__(self):
        return self.title