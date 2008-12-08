import re

from django import template


WIKI_WORD = r'(?:[A-Z]+[a-z]+){2,}'


register = template.Library()


wikifier = re.compile(r'\b(%s)\b' % WIKI_WORD)


@register.filter
def wikify(s):
    from django.core.urlresolvers import reverse
    wiki_root = reverse('wiki.views.index', args=[], kwargs={})
    return wikifier.sub(r'<a href="%s\1/">\1</a>' % wiki_root, s)
