from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from blog.models import Artical


def getIndex(request):
    artical = get_object_or_404(Artical, pk=1)
    return render_to_response('../templates/blog/index.html', {'artical_id': artical.id, 'artical_title': artical.title})


def getArticalDetail(request, id):
    artical = get_object_or_404(Artical, pk=id)
    return render_to_response('../templates/blog/artical_detail.html', {'artical_id': artical.id, 'artical_title': artical.title})
# def getIndex(request):
#
#     try:
#         artical = Artical.objects.get(id=1)
#
#     except Artical.DoesNotExist:
#         raise Http404()
#
#     return render_to_response('../templates/blog/index.html', {'artical': artical})
#
#
# def page_not_found(request):
#     return render_to_response('../templates/blog/404.html')