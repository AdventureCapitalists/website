def site(request):
    return {'SITE_URL': request.site.root_url,
            'SITE_NAME': request.site.site_name}
