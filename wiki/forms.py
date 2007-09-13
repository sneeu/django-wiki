from django import newforms as forms
from django.newforms import widgets

from models import Page


class PageForm(forms.Form):
    name = forms.CharField(max_length=255)
    content = forms.CharField(widget=widgets.Textarea())

    def clean_name(self):
        import re
        from templatetags.wiki import WIKI_WORD

        pattern = re.compile(WIKI_WORD)

        name = self.cleaned_data['name']
        if not pattern.match(name):
            raise forms.ValidationError('Must be a WikiWord.')

        return name