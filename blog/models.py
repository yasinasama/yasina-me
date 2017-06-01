from django.db import models


class Artical(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.ForeignKey('Tag', to_field='tname', db_column='tag')
    image = models.ImageField(upload_to='img/')
    createtime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):

    tname = models.CharField(max_length=20, unique=True)
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tname
