from django.contrib import admin
from blog.models import Artical, Tag, Category


class ArticalAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'createtime']


admin.site.register(Artical, ArticalAdmin)
admin.site.register(Tag)
admin.site.register(Category)
