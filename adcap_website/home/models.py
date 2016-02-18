from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from wagtail.wagtailcore.blocks import BooleanBlock
from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import ChoiceBlock
from wagtail.wagtailcore.blocks import ListBlock
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.blocks import TextBlock
from wagtail.wagtailcore.blocks import URLBlock

from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


''' Blocks '''


class LinkBlock(StructBlock):
    uri = URLBlock(required=True)
    text = CharBlock(required=True)

    class Meta:
        icon = 'link'


class CarouselFrame(StructBlock):
    headline = CharBlock(required=True,
                         help_text='The main, all caps text of the frame.')
    taglines = ListBlock(CharBlock(help_text='The smaller, regular cased text under the '
                                             'headline.'))
    image = ImageChooserBlock(required=True,
                              help_text='The image serving as the background '
                                        'of the frame. Minimum 1080 pixels '
                                        'wide.')
    color = ChoiceBlock(choices=[('dark', 'Dark'),
                                 ('light', 'Light')],
                        icon='cog')
    call_to_action = ListBlock(LinkBlock(classname='call_to_action'),
                               help_text='The large button calling to user to'
                                         'act. Last element receives the '
                                         'most emphasis.')
    signup_form = BooleanBlock(required=False,
                               help_text='Check to display an email '
                                         'signup form in this frame.')

    class Meta:
        icon = 'image'
        template = 'blocks/carousel_frame.html'


'''Page models'''


class HomePage(Page):
    author = models.CharField(max_length=255, blank=True)
    body = StreamField([('heading', CharBlock(classname='full title')),
                        ('carousel', ListBlock(CarouselFrame(),
                                               icon='cogs',
                                               template='blocks/carousel.html',
                                               help_text='A horizontal '
                                                         'scrolling set '
                                                         'of images with text '
                                                         'overlaid.')),
                        ('paragraph', RichTextBlock()),
                        ('image', ImageChooserBlock())], blank=True)

HomePage.content_panels = [FieldPanel('title',
                                      classname='full title'),
                           StreamFieldPanel('body')]
