# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 19:28
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20160221_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title')), (b'carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(help_text=b'The main, all caps text of the frame.', required=True)), (b'taglines', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(help_text=b'The smaller, regular cased text under the headline.'))), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'The image serving as the background of the frame. Minimum 1080 pixels wide.', required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'dark', b'Dark'), (b'light', b'Light')], icon=b'cog')), (b'call_to_action', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'uri', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'text', wagtail.wagtailcore.blocks.CharBlock(required=True))]), help_text=b'Large button to direct user to specific content. Last element has greatest emphasis.', required=False)), (b'signup_form', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check to display an email signup form in this frame.', required=False))]), help_text=b'A horizontal scrolling set of images with text overlaid.', icon=b'cogs', template=b'blocks/carousel.html')), (b'content_row', wagtail.wagtailcore.blocks.StreamBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'promo_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'2', b'2 columns'), (b'3', b'3 columns'), (b'4', b'4 columns'), (b'5', b'5 columns'), (b'6', b'6 columns'), (b'7', b'7 columns'), (b'8', b'8 columns'), (b'9', b'9 columns'), (b'10', b'10 columns'), (b'11', b'11 columns'), (b'12', b'12 columns')], help_text=b'Length in Bootstrap columns for display on desktop.')), (b'offset', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'2', b'2 columns'), (b'3', b'3 columns'), (b'4', b'4 columns'), (b'5', b'5 columns'), (b'6', b'6 columns'), (b'7', b'7 columns'), (b'8', b'8 columns'), (b'9', b'9 columns'), (b'10', b'10 columns'), (b'11', b'11 columns'), (b'12', b'12 columns')], help_text=b'Offset in Bootstrap columns for display on desktop.', required=False)), (b'body', wagtail.wagtailcore.blocks.StreamBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'call_to_action', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'uri', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'button_icon', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'black', b'Black'), (b'white', b'White')])), (b'size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'lg', b'Large'), (b'md', b'Medium'), (b'sm', b'Small')]))]))), (b'spacer', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'15', b'15 pixels'), (b'30', b'30 pixels'), (b'45', b'45 pixels'), (b'60', b'60 pixels'), (b'75', b'75 pixels'), (b'90', b'90 pixels')], required=False))]))]))])), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())], blank=True),
        ),
    ]
