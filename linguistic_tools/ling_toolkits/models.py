from django.db import models

# Create your models here.

class TextData(models.Model):
    content = models.TextField()


class Frequency(models.Model):
    word = models.TextField()
