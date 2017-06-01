from django.shortcuts import render_to_response, Http404
from blog.models import Artical, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from pypinyin import lazy_pinyin


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
    current_artical = Artical.objects.get(title=t)
    return render_to_response('../templates/blog/DetailPage.html', {'current_artical': current_artical})


# def getPinyinTitle(title):
#     try:
#         artical = Artical.objects.get(title=title)
#         return '-'.join(lazy_pinyin(artical.title))
#     except:
#         return 'not-found'


def test(request):
    artical_id = Artical.objects.get(id=1)
    return render_to_response('../templates/blog/DetailPage.html', {'artical_id': artical_id})




