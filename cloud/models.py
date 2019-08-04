from django.db import models

class POST(models.Model):
    title = models.CharField(max_length=100)
    count = models.IntegerField()
    text = models.CharField(max_length=10000)
    