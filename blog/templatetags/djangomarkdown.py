import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(name='djangomarkdown', is_safe=True)
@stringfilter
def djangomarkdown(value):
    return mark_safe(markdown.markdown(value, extras=["code-friendly"]))



