from django.db import models


class Father(models.Model):
    name = models.CharField(max_length=20)


class Son(models.Model):
    father = models.ForeignKey(Father, related_name="sons")
    name = models.CharField(max_length=20)
    book = models.FileField(upload_to="sons/", null=True, blank=True)


class FileModel(models.Model):
    field = models.FileField(upload_to="file/")
