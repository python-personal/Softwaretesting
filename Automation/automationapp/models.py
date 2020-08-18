from django.db import models

# Create your models here.
class enquiry(models.Model):
    name=models.CharField(max_length=90)
    email=models.EmailField()
    message=models.TextField(max_length=900)
    objects=models.Manager()
