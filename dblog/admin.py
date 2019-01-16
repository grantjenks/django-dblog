from django.contrib import admin

from dblog.models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = [
        'create_time',
        'logger',
        'level_name',
        'list_message',
    ]
    readonly_fields = [field.name for field in Record._meta.fields]

    def list_message(self, record):
        lines = record.message.splitlines()
        return lines[0]

    list_message.short_description = 'Message'

admin.site.register(Record, RecordAdmin)
