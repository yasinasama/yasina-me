from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
import blog.views
from lm import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index/(.+)/$', blog.views.getArticalDetail, name='detail'),
    url(r'page/(\d+)', blog.views.getIndex, name='page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = 'blog.views.page_not_found'