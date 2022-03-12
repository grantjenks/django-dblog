from django.contrib import admin
from django.core.paginator import Paginator
from django.utils.functional import cached_property

from dblog.models import Record


class IntPlus(int):
    def __str__(self):
        return '{}+'.format(int.__str__(self))


class LimitCountPaginator(Paginator):
    LIMIT = 10000

    @cached_property
    def count(self):
        """
        Returns the total number of objects, across all pages.
        """
        try:
            limit = self.LIMIT
            total = self.object_list.order_by()[:limit].count()
            # ^-- User order_by() to remove any ordering and
            # count objects as quickly as possible. (Shouldn't
            # SQL optimize the query regardless of ordering?)
            return total if total < limit else IntPlus(total)
        except (AttributeError, TypeError):  # pragma: no cover
            # AttributeError if object_list has no count() method.
            # TypeError if object_list.count() requires arguments
            # (i.e. is of type list).
            return len(self.object_list)


class RecordAdmin(admin.ModelAdmin):
    list_display = [
        'create_time',
        'level_name',
        'list_message',
        'function',
        'module',
        'thread_name',
        'process_name',
    ]
    list_filter = [
        'create_time',
        'level_name',
        'function',
        'module',
        'thread_name',
        'process_name',
    ]
    ordering = ['-create_time']
    readonly_fields = [field.name for field in Record._meta.fields]
    paginator = LimitCountPaginator
    search_fields = ['message']
    show_full_result_count = False

    def list_message(self, record):
        lines = record.message.splitlines()
        line = lines[0]
        line = line[:77] + '...' if len(line) > 77 else line
        return line

    list_message.short_description = 'Message'


admin.site.register(Record, RecordAdmin)
