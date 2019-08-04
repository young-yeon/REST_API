from django.db import models

class POST(models.Model):
    text = models.CharField(max_length=10000)
    