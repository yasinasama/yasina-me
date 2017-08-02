from django.shortcuts import render_to_response
from django.views.generic import View
from django.db.models import *
from blog.models import Artical, Tag, Category
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

    def get(self, request, curpage=1, curartical='', tname='', cname=''):
        artical_list = Artical.objects.all().order_by('-id')
        tags = Tag.objects.all()
        categories = Category.objects.annotate(sum=Count('artical'))
        paginator = Paginator(artical_list, 4)

        if self.template_type == 'detail':
            try:
                current_artical = Artical.objects.get(subtitle=curartical)
                if artical_list[0].id != current_artical.id:
                    later_artical = current_artical.get_next_by_createtime()
                else:
                    later_artical = False
                if artical_list[len(artical_list) - 1].id != current_artical.id:
                    previos_artical = current_artical.get_previous_by_createtime()
                else:
                    previos_artical = False
            except ObjectDoesNotExist:
                return render_to_response('../templates/blog/404.html')
        else:
            current_artical = ''
            later_artical = False
            previos_artical = False

        if self.template_type == 'tagarticals':
            try:
                curtag = Tag.objects.get(tname=tname)
                articals = Artical.objects.filter(tag=tname).all().order_by('-id')
            except ObjectDoesNotExist:
                return render_to_response('../templates/blog/404.html')
        else:
            curtag = ''
            articals = []

        if self.template_type == 'categoryarticals':
            try:
                curcategory = Category.objects.get(cname=cname)
                articals_category = Artical.objects.filter(category=cname).all().order_by('-id')
            except ObjectDoesNotExist:
                return render_to_response('../templates/blog/404.html')
        else:
            curcategory = ''
            articals_category = []

        tag_more_items = Artical.objects.values('tag').annotate(sum=Count('tag')).order_by('-sum')[:tags.count() // 3]
        tag_more_name = [tag_name.get('tag') for tag_name in tag_more_items]

        category_more_items = Artical.objects.values('category').annotate(sum=Count('category')).order_by('-sum')[:categories.count() // 3]
        category_more_name = [category_name.get('category') for category_name in category_more_items]

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
            'categories': categories,
            'current_artical': current_artical,
            'curtag': curtag,
            'articals': articals,
            'curcategory': curcategory,
            'articals_category': articals_category,
            'tag_more_name': tag_more_name,
            'category_more_name': category_more_name,
            'artical_curpage': artical_curpage,
            'paginator': paginator,
        }
        return render_to_response('../templates/blog/' + self.template_name, context)
