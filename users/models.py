from django.db import models


class Reg_Details(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=30)
