from django.contrib import admin
from blog.models import Artical, Tag


admin.site.register((Tag, Artical))
