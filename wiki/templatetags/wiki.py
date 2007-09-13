import re

from django import template

WIKI_WORD = r'(?:[A-Z]+[a-z]+){2,}'


register = template.Library()


wikifier = re.compile(r'\b(%s)\b' % WIKI_WORD)


@register.filter
def wikify(s):
    return wikifier.sub(r'<a href="/\1/">\1</a>', s)