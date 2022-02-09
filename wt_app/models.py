from django.db import models
from cloudinary.models import CloudinaryField
class Wb(models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    img = CloudinaryField('img')
    username = models.CharField(max_length=100)
    Email_id = models.CharField(max_length=100)
    psw = models.CharField(max_length=100)
    line_1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class SB(models.Model):
    first_Name1 = models.CharField(max_length=100)
    last_Name1 = models.CharField(max_length=100)
    img1 = CloudinaryField('img1')
    username1 = models.CharField(max_length=100)
    Email_id1 = models.CharField(max_length=100)
    psw1 = models.CharField(max_length=100)
    line_11 = models.CharField(max_length=100)
    city1 = models.CharField(max_length=100)
    state1 = models.CharField(max_length=100)
    pincode1 = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
