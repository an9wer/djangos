from django.db import models


class Father(models.Model):
    name = models.CharField(max_length=20)


class Son(models.Model):
    father = models.ForeignKey(Father, related_name="sons")
    name = models.CharField(max_length=20)
    book = models.FileField(upload_to="sons/", null=True, blank=True)


class FileModel(models.Model):
    field = models.FileField(upload_to="file/")


class CharModel(models.Model):
    field = models.CharField(max_length=20)

    def __str__(self):
        return self.field


class OTTModel(models.Model):
    one = models.CharField(max_length=20)
    two = models.CharField(max_length=20)
    three = models.CharField(max_length=20)
