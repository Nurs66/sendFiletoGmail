from django.contrib import admin

from sms_sender.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    list_filter = ('first_name', 'last_name', 'phone_number')
    search_fields = ('first_name', 'last_name',)


admin.site.register(Person, PersonAdmin)
