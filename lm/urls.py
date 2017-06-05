from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
import blog.views
from lm import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^detail/(.+)', blog.views.getDetailPage, name='detail'),
    url(r'^page/(\d+)', blog.views.getAnotherPage, name='page'),
    url(r'^tag/(.+)', blog.views.getTagArticals, name='tag_articals'),
    url(r'^tag/', blog.views.getTagPage, name='tag'),
    url(r'^archive/', blog.views.getArchivePage, name='archive'),
    url(r'^aboutme/', blog.views.getAboutMePage, name='aboutme'),
    url(r'^$', blog.views.getMainPage, name='mainpage'),
    url(r'test', blog.views.test)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



