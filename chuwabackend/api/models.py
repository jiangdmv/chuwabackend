from django.db import models


# Upload file API
class FileModel(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='upload')    # store the file at /upload/ folder


class TestAPIModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    file = models.FileField(upload_to='upload')    # store the file at /upload/ folder
