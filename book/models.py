from distutils.command.upload import upload
from email.policy import default
from enum import unique
from multiprocessing import AuthenticationError
from django.db import models
from autoslug import AutoSlugField
class Book(models.Model):
    book_name=models.CharField(max_length=50)
    book_des=models.CharField(max_length=50)
    book_image = models.ImageField(upload_to="book/",  null=True,)
    book_slug = AutoSlugField(populate_from='book_name',unique=True ,null=True, )

# Create your models here.
