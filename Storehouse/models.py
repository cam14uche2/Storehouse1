from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

        def get_absolute_url(self):
            return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    #created = models.DateTimeField(auto_now_add=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, default='coding')
    Snippet = models.CharField(max_length=200)
    #likes = models.ManyToManyField(User, related_name='writeup_posts')

    # def total_likes(self):
    #    return self.likes.count()

    # def __str___(self):
        #return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')  


