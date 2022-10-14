import hashlib
import string
from random import choice

from urlshort.interface import BaseSlugCreator


class BasicSlugCreatorService(BaseSlugCreator):

    def get_slug(self, *args, **kwargs) -> str:
        """Function to generate short_id of specified number of characters"""
        return ''.join(
            choice(string.ascii_letters + string.digits)
            for _ in range(self.length))


class MD5SlugCreatorService(BaseSlugCreator):

    def get_slug(self, *args, **kwargs) -> str:
        """
        Uses characters from start of MD5 of original url
        """
        original_url = kwargs.get('original_url', None)
        return hashlib.md5(original_url.encode()).hexdigest()[:self.length]
