from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    desc=models.CharField(max_length=200)
    url=models.CharField(max_length=200)

def __str__(self):
    return self.title