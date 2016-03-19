from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from wagtail.wagtailcore.blocks import ListBlock

from blocks import CarouselFrame
from blocks import ShortHeroBlock
from blocks import ContentRow
from blocks import QuotationsBlock
from blocks import StatsBlock
from blocks import StatementBlock
from blocks import TeamMemberBlock
from blocks import SoundCloudBlock


class HomePage(Page):
    body = StreamField([('carousel', ListBlock(CarouselFrame(),
                                               icon='cogs',
                                               template='blocks/carousel.html',
                                               help_text='A horizontal '
                                                         'scrolling set '
                                                         'of images with text '
                                                         'overlaid.')),
                        ('short_hero', ShortHeroBlock()),
                        ('content_row', ContentRow()),
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
