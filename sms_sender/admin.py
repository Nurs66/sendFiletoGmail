from django.contrib import admin

from sms_sender.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone_number', 'email')
    list_filter = ('fio', 'phone_number')
    search_fields = ('fio',)


admin.site.register(Person, PersonAdmin)
