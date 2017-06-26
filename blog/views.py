from django.shortcuts import render_to_response, Http404, get_object_or_404
from django.views.generic import View
from django.db.models import *
from blog.models import Artical, Tag
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "/feed/"
    description = "RSS feed - blog posts"

    def items(self):
        return Artical.objects.order_by('-createtime')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


class TemplateView(View):
    template_name = ''
    template_type = ''

    def get(self, request, curpage=1, curartical='', tname=''):
        artical_list = Artical.objects.all().order_by('-id')
        tags = Tag.objects.all()
        paginator = Paginator(artical_list, 4)

        if self.template_type == 'detail':
            current_artical = get_object_or_404(Artical, title=curartical)
            if artical_list[0].id != current_artical.id:
                later_artical = current_artical.get_next_by_createtime()
            else:
                later_artical = False
            if artical_list[len(artical_list) - 1].id != current_artical.id:
                previos_artical = current_artical.get_previous_by_createtime()
            else:
                previos_artical = False
        else:
            current_artical = ''
            later_artical = False
            previos_artical = False

        if self.template_type == 'tagarticals':
            curtag = Tag.objects.get(tname=tname)
            articals = Artical.objects.filter(tag=tname).all()
        else:
            curtag = ''
            articals = []

        tag_more_items = Artical.objects.values('tag').annotate(sum=Count('tag')).order_by('-sum')[:tags.count() // 3]
        tag_more_name = [tag_name.get('tag') for tag_name in tag_more_items]

        try:
            artical_curpage = paginator.page(curpage)
        except PageNotAnInteger:
            artical_curpage = paginator.page(1)
        except EmptyPage:
            artical_curpage = paginator.page(paginator.num_pages)

        context = {
            'artical_list': artical_list,
            'later_artical': later_artical,
            'previos_artical': previos_artical,
            'tags': tags,
            'current_artical': current_artical,
            'curtag': curtag,
            'articals': articals,
            'tag_more_name': tag_more_name,
            'artical_curpage': artical_curpage,
            'paginator': paginator,
        }
        return render_to_response('../templates/blog/' + self.template_name, context)
