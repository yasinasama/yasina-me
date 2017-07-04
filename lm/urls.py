from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
import blog.views
from blog.views import RSSFeed
from lm import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^detail/(?P<curartical>.+)', blog.views.TemplateView.as_view(template_name='DetailPage.html', template_type='detail'), name='detail'),
    url(r'^page/(?P<curpage>\d+)', blog.views.TemplateView.as_view(template_name='MainPage.html'), name='page'),
    url(r'^tag/(?P<tname>.+)', blog.views.TemplateView.as_view(template_name='TagArticals.html', template_type='tagarticals'), name='tag_articals'),
    url(r'^tag/', blog.views.TemplateView.as_view(template_name='TagPage.html'), name='tag'),
    url(r'^archive/', blog.views.TemplateView.as_view(template_name='ArchivePage.html'), name='archive'),
    url(r'^category/(?P<cname>.+)', blog.views.TemplateView.as_view(template_name='CategoryArticals.html', template_type='categoryarticals'), name='category_articals'),
    url(r'^category/', blog.views.TemplateView.as_view(template_name='CategoryPage.html'), name='category'),
    url(r'^aboutme/', blog.views.TemplateView.as_view(template_name='AboutMe.html'), name='aboutme'),
    url(r'^feed/', RSSFeed(), name="RSS"),
    url(r'^$', blog.views.TemplateView.as_view(template_name='MainPage.html'), name='mainpage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



