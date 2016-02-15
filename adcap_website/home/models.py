from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HomePage(Page):
    author = models.CharField(max_length=255, blank=True)
    date = models.DateField("Post date", blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], blank=True)

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('author'),
    FieldPanel('date'),
    StreamFieldPanel('body'),
]
