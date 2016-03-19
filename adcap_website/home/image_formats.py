from wagtail.wagtailimages.formats import Format, register_image_format

register_image_format(Format('pull-left', 'Pull Left Wx200', 'pull-left img-responsive img-thumbnail', 'fill-200x250-c100'))
register_image_format(Format('pull-right', 'Pull Right Wx200', 'pull-right img-responsive img-thumbnail', 'fill-200x250-c100'))
