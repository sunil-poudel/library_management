from django.db import models

# Create your models here.
class Note(models.Model):
    date = models.DateField()
    plan = models.TextField()

    def __str__(self):
        return self.plan
