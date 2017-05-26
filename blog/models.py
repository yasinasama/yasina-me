from django.db import models


class Artical(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='img/')
    createtime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title