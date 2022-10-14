from operator import concat

from django.conf import settings
from django.db import models
from django.db.models import CharField, Value
from django.db.models.functions import Concat

# Create your models here.
from omnicommon.models import BaseDateTimeUUIDModel


class Short(BaseDateTimeUUIDModel):
    '''
    Base class for ALL shortner Entities

    This class will hold common columns like "click_count"
    '''

    class Meta:
        abstract = True


class BuiltInURLManager(models.Manager):

    def get_queryset(self):
        return super(BuiltInURLManager,
                     self).get_queryset().annotate(full_url=Concat(
                         Value(f'{settings.LOCAL_DOMAIN_NAME}'),
                         'slug',
                         output_field=CharField(),
                     )).values()


class URLShort(Short):
    '''
    Child class of Short

    Implements URL shortner
    '''
    objects = models.Manager()
    built_in_urls = BuiltInURLManager()

    original_url = models.TextField(null=False, blank=False)
    slug = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = 'URL Short'
        verbose_name_plural = 'URL Short'
