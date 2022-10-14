from django.contrib import admin
from django.utils.translation import gettext as _


# Register your models with this base class.
class BaseUUIDAdmin(admin.ModelAdmin):

    readonly_fields = (
        'uuid',
        'created_at',
        'modified_at',
    )


class InputFilter(admin.SimpleListFilter):
    # Generic Input Filter
    # ref: https://hakibenita.com/how-to-add-a-text-filter-to-django-admin

    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((), )

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = ((
            k, v) for k, v in changelist.get_filters_params().items()
                                     if k != self.parameter_name)
        yield all_choice


class SlugSearch(InputFilter):
    # works with a "slug" column in the model
    # ref: https://hakibenita.com/how-to-add-a-text-filter-to-django-admin

    # what it'll be called in the url
    parameter_name = 'slug'

    # what will show up on UI
    title = _('slug')

    def queryset(self, request, queryset):
        if self.value() is not None:
            name = self.value()

            return queryset.filter(slug__icontains=name)
