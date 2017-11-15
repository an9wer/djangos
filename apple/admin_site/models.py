from django.db import models

class AdminModel(models.Model):
    field = models.CharField(max_length=20)
