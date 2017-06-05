from django.contrib import admin
from blog.models import Artical, Tag


class ArticalAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'createtime']


admin.site.register(Artical, ArticalAdmin)
admin.site.register(Tag)
