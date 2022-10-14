from enum import unique
from statistics import mode
from textwrap import indent
from unittest.util import _MAX_LENGTH

from django.db import models

# Create your models here.
from omnicommon.models import BaseDateTimeUUIDModel


class Short(BaseDateTimeUUIDModel):
    '''
    Base class for ALL shortner Entities

    This class will hold common columns like "click_count"
    '''

    class Meta:
        abstract = True


class URLShort(Short):
    '''
    Child class of Short

    Implements URL shortner
    '''
    original_url = models.TextField(null=False, blank=False)
    slug = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = 'URL Short'
        verbose_name_plural = 'URL Short'
