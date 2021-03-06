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
from wagtail.wagtailimages.blocks import ImageChooserBlock

from home.blocks import CarouselFrame
from home.blocks import ShortHeroBlock
from home.blocks import SectionBlock
from home.blocks import QuotationsBlock
from home.blocks import StatsBlock
from home.blocks import StatementBlock
from home.blocks import TeamMemberBlock
from home.blocks import SoundCloudBlock
from home.blocks import SidebarCallOutBlock
from home.blocks import CallToActionBlock
from home.blocks import ContentCarouselFrame

from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.models import register_setting


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
                        ('soundcloud', SoundCloudBlock()),
                        ('section_carousel', ListBlock(ImageChooserBlock(),
                                                       icon='image',
                                                       template='blocks/'
                                                                'section_'
                                                                'carousel'
                                                                '.html')),
                        ('content_carousel', ListBlock(ContentCarouselFrame(),
                                                       icon='image',
                                                       template='blocks/'
                                                                'content_'
                                                                'carousel'
                                                                '.html'))],
                       blank=True)
    search_image = models.ForeignKey('wagtailimages.Image',
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL,
                                     related_name='+')

    social_image = models.ForeignKey('wagtailimages.Image',
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL,
                                     related_name='+')

HomePage.content_panels = [FieldPanel('title'),
                           StreamFieldPanel('body')]

HomePage.promote_panels = [MultiFieldPanel(Page.promote_panels,
                                           "Common Configuration"),
                           ImageChooserPanel('search_image'),
                           ImageChooserPanel('social_image')]


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


@register_setting(icon='user')
class SocialMediaSettings(BaseSetting):
    facebook = models.CharField(max_length=255,
                                null=True,
                                blank=True,
                               help_text="Your Facebook handle")
    instagram = models.CharField(max_length=255,
                                 null=True,
                                 blank=True,
                                 help_text="Your Instagram handle")
    twitter = models.CharField(max_length=255,
                               null=True,
                               blank=True,
                               help_text="Your Twitter handle")
    github = models.CharField(max_length=255,
                              null=True,
                              blank=True,
                              help_text="Your GitHub username")
    soundcloud = models.CharField(max_length=255,
                                  null=True,
                                  blank=True,
                                  help_text="Your SoundCloud username")


@register_setting(icon='site')
class ExternalServicesSettings(BaseSetting):
    google_analytics = models.CharField(max_length=255,
                                        null=True,
                                        blank=True,
                                        help_text="Your Google Analytics UA")
    google_tag_manager = models.CharField(max_length=255,
                                          null=True,
                                          blank=True,
                                          help_text="Your Google Tag Manager "
                                                    "GTM ID")
    optimizely = models.CharField(max_length=255,
                                  null=True,
                                  blank=True,
                                  help_text="Your Optimizely project ID")
    disqus = models.CharField(max_length=255,
                              null=True,
                              blank=True,
                              help_text="Your Disqus community name")
    mailchimp_u = models.CharField(max_length=255,
                                   null=True,
                                   blank=True,
                                   help_text="Your MailChimp user ID")
    mailchimp_id = models.CharField(max_length=255,
                                    null=True,
                                    blank=True,
                                    help_text="Your MailChimp List ID")
