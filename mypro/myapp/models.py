from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class task(models.Model):
    email = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.email
