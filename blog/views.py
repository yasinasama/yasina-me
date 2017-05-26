from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from blog.models import Artical
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def getIndex(request, curpage):
    artical_list = Artical.objects.all()
    paginator = Paginator(artical_list, 3)
    try:
        page = paginator.page(curpage)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render_to_response('../templates/blog/index.html', {'artical_list': page})


def getArticalDetail(request, id):
    artical_id = Artical.objects.get(id=id)
    return render_to_response('../templates/blog/artical_detail.html', {'artical_id': artical_id})


