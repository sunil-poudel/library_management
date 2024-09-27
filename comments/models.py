from django.db import models

# Create your models here.
class Comment(models.Model):
    comments = models.TextField()
    books = models.ForeignKey("books.Book", on_delete=models.CASCADE)

    def __str__(self):
        return self.comments