from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query

from home.models import HomePage


def search(request):
    search_query = request.GET.get('q', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        search_results = HomePage.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
        'search_title': "Search for Adventure Capitalists: {0}".format(search_query)
    })
