import markdown
import urllib
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='djangomarkdown', is_safe=True)
@stringfilter
def djangomarkdown(value):
    return mark_safe(markdown.markdown(value, extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ]))


@register.filter(name='urlchange', is_safe=True)
@stringfilter
def urlchange(value):
    return urllib.parse.quote(value)



