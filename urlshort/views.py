# Create your views here.
from django.http import Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from urlshort.api import URLShortAPI
from urlshort.models import URLShort
from urlshort.services import BasicSlugCreatorService, MD5SlugCreatorService


@csrf_exempt
def make_short(request):
    print(request.__dict__)
    print(request.method)
    original_url = request.POST.get('original_url', None)
    message = 'Show All Records'
    if original_url:

        # TODO:
        # Current approch supports easy switch between Slug Creator Service
        # Implement Controller patternt to avoid changes in views.py

        # Select Service

        # Use MD5 Slug Creator
        # service = MD5SlugCreatorService(7)

        # Use Basic Slug Creator
        service = BasicSlugCreatorService(10)

        short_api = URLShortAPI(service)
        short_row = short_api.create(original_url)
        if short_row:
            message = 'Record Added'
        else:
            message = 'Error in record creation'

    shorts = URLShort.built_in_urls.all()
    template = 'make_short.html'
    return render(request, template, {
        'shorts': shorts,
        'message': message,
    })


@csrf_exempt
def redirect_slug(request, slug=None):
    if not slug:
        return HttpResponseBadRequest()
    short_row = URLShortAPI.get(slug)
    if not short_row:
        raise Http404
    return HttpResponseRedirect(short_row.original_url)
