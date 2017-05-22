from django.conf.urls import url
from django.contrib import admin
import blog.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index/', blog.views.getIndex),
]
