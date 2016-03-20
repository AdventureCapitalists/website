from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailforms.models import AbstractEmailForm
from wagtail.wagtailforms.models import AbstractFormField

from wagtail.wagtailcore.blocks import ListBlock

from blocks import CarouselFrame
from blocks import ShortHeroBlock
from blocks import SectionBlock
from blocks import QuotationsBlock
from blocks import StatsBlock
from blocks import StatementBlock
from blocks import TeamMemberBlock
from blocks import SoundCloudBlock
from blocks import SidebarCallOutBlock
from blocks import CallToActionBlock


class HomePage(Page):
    body = StreamField([('carousel', ListBlock(CarouselFrame(),
                                               icon='cogs',
                                               template='blocks/carousel.html',
                                               help_text='A horizontal '
                                                         'scrolling set '
                                                         'of images with text '
                                                         'overlaid.')),
                        ('short_hero', ShortHeroBlock()),
                        ('section', SectionBlock()),
                        ('quotations', QuotationsBlock()),
                        ('stats', StatsBlock()),
                        ('statement', StatementBlock()),
                        ('team_carousel', ListBlock(TeamMemberBlock(),
                                                    icon='group',
                                                    template='blocks/'
                                                             'team_carousel.'
                                                             'html')),
                        ('soundcloud', SoundCloudBlock())],
                       blank=True)

HomePage.content_panels = [FieldPanel('title'),
                           StreamFieldPanel('body')]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    intro = RichTextField(blank=True)
    sidebar = StreamField([('callout', SidebarCallOutBlock()),
                           ('call_to_action', CallToActionBlock())])
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('hero'),
        FieldPanel('intro'),
        StreamFieldPanel('sidebar'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldPanel('to_address', classname="full"),
            FieldPanel('from_address', classname="full"),
            FieldPanel('subject', classname="full"),
        ], "Email")
    ]
