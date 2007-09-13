from django.db import models

from templatetags.wiki import wikify


class Page(models.Model):
    name = models.CharField(maxlength=255, unique=True)
    content = models.TextField()
    rendered = models.TextField()

    class Admin:
        fields = (
            None, {
                'fields': ('name', 'content',)
            }
        )

    def save(self):
        self.rendered = wikify(self.content)
        super(Page, self).save()

    def __str__(self):
        return '%s\n%s\n\n%s' % (self.name, '-' * 40, self.content)