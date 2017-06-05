from django.shortcuts import render_to_response, Http404, get_object_or_404
from markdown import markdown

from blog.models import Artical, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def getMainPage(request):
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    artical_list = paginator.page(1)
    tag_count = Tag.objects.count()
    return render_to_response('../templates/blog/MainPage.html', {'artical_list': artical_list,
                                                                  'paginator': paginator,
                                                                  'tag_count': tag_count})


def getAnotherPage(request, curpage):
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)

    tag_count = Tag.objects.count()
    try:
        artical_list = paginator.page(curpage)
    except PageNotAnInteger:
        artical_list = paginator.page(1)
    except EmptyPage:
        artical_list = paginator.page(paginator.num_pages)
    return render_to_response('../templates/blog/MainPage.html', {'artical_list': artical_list,
                                                                  'paginator': paginator,
                                                                  'tag_count': tag_count})


def getDetailPage(request, t):
    current_artical = get_object_or_404(Artical, title=t)
    current_artical.content = markdown(current_artical.content, extras=['fenced-code-blocks'])
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    tag_count = Tag.objects.count()
    return render_to_response('../templates/blog/DetailPage.html', {'current_artical': current_artical,
                                                                    'paginator': paginator,
                                                                    'tag_count': tag_count})


def getTagPage(request):
    tags = Tag.objects.all()
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    tag_count = Tag.objects.count()
    return render_to_response('../templates/blog/TagPage.html', {'tags': tags,
                                                                 'paginator': paginator,
                                                                 'tag_count': tag_count})


def getArchivePage(request):
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    tag_count = Tag.objects.count()
    return render_to_response('../templates/blog/ArchivePage.html', {'artical_list': artical_list,
                                                                     'paginator': paginator,
                                                                     'tag_count': tag_count})


def getAboutMePage(request):
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    tag_count = Tag.objects.count()
    return render_to_response('../templates/blog/AboutMe.html', {'paginator': paginator,
                                                                 'tag_count': tag_count})


def getTagArticals(request, tname):
    curtag = Tag.objects.get(tname=tname)
    articals = Artical.objects.filter(tag=tname).all()
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    tag_count = Tag.objects.count()
    return render_to_response('../templates/blog/TagArticals.html', {'paginator': paginator,
                                                                     'tag_count': tag_count,
                                                                     'curtag': curtag,
                                                                     'articals': articals})


def test(request):
    body = '''```python
           hello world
           '''
    return render_to_response('../templates/blog/test.html', {'body': body})
