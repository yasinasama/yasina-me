from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from blog.models import Artical
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def getMainPage(request):
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    artical_list = paginator.page(1)

    return render_to_response('../templates/blog/index.html', {'artical_list': artical_list, 'paginator': paginator})


def getIndex(request, curpage):
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    try:
        artical_list = paginator.page(curpage)
    except PageNotAnInteger:
        artical_list = paginator.page(1)
    except EmptyPage:
        artical_list = paginator.page(paginator.num_pages)
    return render_to_response('../templates/blog/index.html', {'artical_list': artical_list, 'paginator': paginator})


def getArticalDetail(request, id):
    artical_id = Artical.objects.get(id=id)
    return render_to_response('../templates/blog/artical_detail.html', {'artical_id': artical_id})


