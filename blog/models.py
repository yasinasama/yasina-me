from django.db import models
from django.urls import reverse


class Artical(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    tag = models.ForeignKey('Tag', to_field='tname', db_column='tag')
    category = models.ForeignKey('Category', to_field='cname', db_column='category', default=None)
    image = models.ImageField(upload_to='img/')
    createtime = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('detail', args=[1])

    def __str__(self):
        return self.title


class Tag(models.Model):

    tname = models.CharField(max_length=20, unique=True)
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tname


class Category(models.Model):

    cname = models.CharField(max_length=20, unique=True)
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cname
