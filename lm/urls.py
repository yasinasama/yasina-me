from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
import blog.views
from lm import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'detail/(.*)', blog.views.getDetailPage, name='detail'),
    url(r'page/(\d+)', blog.views.getAnotherPage, name='page'),
    url(r'^$', blog.views.getMainPage, name='page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



