from django.shortcuts import render

from wagtail.wagtailsearch.models import Query

from .models import HomePage


def search(request):
    # Search
    search_query = request.GET.get('q', None)
    if search_query:
        search_results = HomePage.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = HomePage.objects.none()

    # Render template
    return render(request, 'search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
        'search_title': "Search for Adventure Capitalists: {0}".format(search_query)
    })
