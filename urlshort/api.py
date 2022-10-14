from django.db.utils import IntegrityError

from urlshort.exceptions import ServiceNotInitialized
from urlshort.interfaces import BaseSlugCreator
from urlshort.models import URLShort


class URLShortAPI:

    MAX_RETRY = 5

    def __init__(self, shortner_service: BaseSlugCreator = None) -> None:
        self.shortner_service = shortner_service

    def create(self, original_url: str) -> URLShort:
        # check service type
        if not self.shortner_service:
            raise ServiceNotInitialized(
                'Service is empty. Must be child of BaseSlugCreator')

        while self.MAX_RETRY > 0:
            slug = self.shortner_service.get_slug(original_url=original_url)
            try:
                short_row = URLShort.objects.create(slug=slug)
                short_row.original_url = original_url
                short_row.save()
                return short_row
            except IntegrityError:
                self.MAX_RETRY -= 1

        return None

    @classmethod
    def get(cls, slug: str):
        try:
            return URLShort.objects.get(slug=slug)
        except URLShort.DoesNotExist:
            return None
