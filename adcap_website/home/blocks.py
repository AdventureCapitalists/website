from wagtail.wagtailcore.blocks import BooleanBlock
from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import ChoiceBlock
from wagtail.wagtailcore.blocks import ListBlock
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.blocks import StructBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock


class LinkBlock(StructBlock):
    uri = CharBlock(required=True)
    text = CharBlock(required=False)
    icon = CharBlock(required=False)

    class Meta:
        icon = 'link'


class CallToActionBlock(LinkBlock):
    color = ChoiceBlock([('black', 'Black'),
                         ('white', 'White')],
                        required=True)
    size = ChoiceBlock([('lg', 'Large'),
                        ('md', 'Medium'),
                        ('sm', 'Small'),
                        ('xs', 'Extra Small')])

    class Meta:
        icon = 'link'
        template = 'blocks/call_to_action.html'


class CarouselFrame(StructBlock):
    headline = CharBlock(required=True,
                         help_text='The main, all caps text of the frame.')
    taglines = ListBlock(CharBlock(help_text='The smaller, regular cased text '
                                             'under the headline.'))
    image = ImageChooserBlock(required=True,
                              help_text='The image serving as the background '
                                        'of the frame. Minimum 1080 pixels '
                                        'wide.')
    color = ChoiceBlock(choices=[('dark', 'Dark'),
                                 ('light', 'Light')],
                        icon='cog')
    call_to_action = ListBlock(LinkBlock(),
                               required=False,
                               help_text='Large button to direct user to '
                                         'specific content. Last element '
                                         'has greatest emphasis.')
    signup_form = BooleanBlock(required=False,
                               help_text='Check to display an email '
                                         'signup form in this frame.')

    class Meta:
        icon = 'image'
        template = 'blocks/carousel_frame.html'


class ContentBlock(StructBlock):
    width = ChoiceBlock(choices=[('2', '2 columns'),
                                 ('3', '3 columns'),
                                 ('4', '4 columns'),
                                 ('5', '5 columns'),
                                 ('6', '6 columns'),
                                 ('7', '7 columns'),
                                 ('8', '8 columns'),
                                 ('9', '9 columns'),
                                 ('10', '10 columns'),
                                 ('11', '11 columns'),
                                 ('12', '12 columns')],
                        required=True,
                        help_text='Length in Bootstrap columns for '
                                  'display on desktop.')
    offset = ChoiceBlock(choices=[('2', '2 columns'),
                                  ('3', '3 columns'),
                                  ('4', '4 columns'),
                                  ('5', '5 columns'),
                                  ('6', '6 columns'),
                                  ('7', '7 columns'),
                                  ('8', '8 columns'),
                                  ('9', '9 columns'),
                                  ('10', '10 columns'),
                                  ('11', '11 columns'),
                                  ('12', '12 columns')],
                         required=False,
                         help_text='Offset in Bootstrap columns for '
                                   'display on desktop.')
    align = ChoiceBlock(choices=[('text-left', 'Left aligned text'),
                                 ('text-center', 'Center aligned text'),
                                 ('text-right', 'Right aligned text'),
                                 ('text-justify', 'Justified text'),
                                 ('text-nowrap', 'No wrap text')],
                        required=False,
                        help_text='Alignment for text in content block.')

    class Meta:
        icon = 'doc-empty'


class PromoParagraphBlock(ContentBlock):
    body = StreamBlock([('text', RichTextBlock()),
                        ('call_to_action', ListBlock(CallToActionBlock())),
                        ('spacer', ChoiceBlock(choices=[('15', '15 pixels'),
                                                        ('30', '30 pixels'),
                                                        ('45', '45 pixels'),
                                                        ('60', '60 pixels'),
                                                        ('75', '75 pixels'),
                                                        ('90', '90 pixels')],
                                               required=False))])

    class Meta:
        template = 'blocks/promo_paragraph.html'
        icon = 'doc-full'


class SkillbarBlock(ContentBlock):

    skills = ListBlock(StructBlock([('skill_percentage', CharBlock()),
                                    ('skill_name', CharBlock())]))

    class Meta:
        icon = 'form'
        template = 'blocks/skillbar.html'


class IconBlurbBlock(ContentBlock):
    icon = CharBlock(help_text='Text block passed as the icon selected. '
                               'Choose between Ionic Icons or FontAwesome.')
    headline = CharBlock(required=False)
    body = RichTextBlock(required=False)

    class Meta:
        icon = 'image'
        template = 'blocks/icon_blurb.html'


class DefinitionListBlock(ContentBlock):
    definitions = ListBlock(StructBlock([('title', CharBlock()),
                                         ('definition', CharBlock())]))

    class Meta:
        icon = 'tag'
        template = 'blocks/definition_list.html'


class SidebarCallOutBlock(StructBlock):
    title = CharBlock()
    body = RichTextBlock(required=False)
    icon = CharBlock(required=False,
                     help_text='Text block passed as the icon selected. '
                               'Choose between Ionic Icons or FontAwesome.')
    links = ListBlock(LinkBlock(),
                      required=False)

    class Meta:
        icon = 'radio-empty'
        template = 'blocks/sidebar_callout.html'


class SectionBlock(StreamBlock):
    promo_paragraph = PromoParagraphBlock()
    skillbar = SkillbarBlock()
    icon_blurb = IconBlurbBlock()
    definition_list = DefinitionListBlock()
    callout = SidebarCallOutBlock()

    class Meta:
        icon = 'folder'
        template = 'blocks/content_row.html'


class ParallaxBlock(StructBlock):
    image = ImageChooserBlock(required=True,
                              help_text='The image serving as the background '
                                        'of the quotations. Minimum 1080 '
                                        'pixels wide.')
    color = ChoiceBlock([('light', 'Light'),
                         ('dark', 'Dark')])


class QuoteBlock(StructBlock):
    quotation = CharBlock()
    author = CharBlock(required=False)
    title = CharBlock(required=False)

    class Meta:
        icon = 'openquote'


class QuotationsBlock(ParallaxBlock):
    quotations = ListBlock(QuoteBlock())

    class Meta:
        icon = 'openquote'
        template = 'blocks/quotations.html'


class StatBlock(StructBlock):
    label = CharBlock()
    count = CharBlock()


class StatsBlock(ParallaxBlock):
    stats = ListBlock(StatBlock())

    class Meta:
        icon = 'list-ol'
        template = 'blocks/stats.html'


class ShortHeroBlock(StructBlock):
    image = ImageChooserBlock(required=True,
                              help_text='The image serving as the header '
                                        'image for the page. Shorter '
                                        'than the carousel, intended '
                                        'for sub pages.')
    color = ChoiceBlock([('light', 'Light'),
                         ('dark', 'Dark')])
    title = CharBlock()
    subtitle = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = 'blocks/short_hero.html'


class StatementBlock(StructBlock):
    title = CharBlock()
    subtitles = ListBlock(CharBlock(required=False),
                          required=False)
    call_to_action = ListBlock(CallToActionBlock(),
                               required=False,
                               help_text='Large button to direct user to '
                                         'specific content. Last element '
                                         'has greatest emphasis.')
    signup_form = BooleanBlock(required=False,
                               help_text='Check to display an email '
                                         'signup form in this frame.')
    caveats = ListBlock(CharBlock(required=False),
                        required=False)

    class Meta:
        icon = 'pilcrow'
        template = 'blocks/statement.html'


class SoundCloudBlock(StructBlock):
    track_id = CharBlock(required=False)
    playlist_id = CharBlock(required=False)
    auto_play = BooleanBlock(required=False)
    hide_related = BooleanBlock(required=False)
    show_comments = BooleanBlock(required=False)
    show_user = BooleanBlock(required=False)
    show_reposts = BooleanBlock(required=False)
    visual = BooleanBlock(required=False)

    class Meta:
        icon = 'media'
        template = 'blocks/soundcloud.html'


class TeamMemberBlock(StructBlock):
    name = CharBlock()
    title = CharBlock(required=False)
    qualifications = CharBlock(required=False)
    image = ImageChooserBlock()
    links = ListBlock(LinkBlock(),
                      required=False)

    class Meta:
        icon = 'user'
        template = 'blocks/team_member.html'


class ContentCarouselFrame(StructBlock):
    image = ImageChooserBlock()
    image_location = ChoiceBlock([('left', 'Left'),
                                  ('right', 'Right')],
                                required=False)
    description = PromoParagraphBlock()

    class Meta:
        icon = 'image'
        template = 'blocks/content_carousel_frame.html'
