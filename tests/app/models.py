from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from modelcluster.fields import ParentalKey

from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsnippets.models import register_snippet

from wagtailnews.models import NewsIndexMixin, AbstractNewsItem
from wagtailnews.decorators import newsindex


class NewsIndexTag(TaggedItemBase):
    content_object = ParentalKey('NewsIndex', related_name='tagged_items')


class NewsItemTag(TaggedItemBase):
    content_object = ParentalKey('NewsItem', related_name='tagged_items')


@newsindex
class NewsIndex(NewsIndexMixin, Page):
    newsitem_model = 'NewsItem'


@register_snippet
@python_2_unicode_compatible
class NewsItem(AbstractNewsItem):
    title = models.CharField(max_length=32)

    tags = TaggableManager(through=NewsItemTag, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('tags'),
        FieldPanel('date'),
    ]

    def __str__(self):
        return self.title
