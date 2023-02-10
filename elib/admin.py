from django.contrib import admin

from .models import (message, student, staff, publication, book,
                     lecture_note, leasing, reading_list, gen_login)


class booksAdmin(admin.ModelAdmin):
    search_fields = ["title", "author", "department"]
    list_filter = ["department", "visibility"]
    readonly_fields = ['id', ]
    # list_editable = ["property_price"]
    # list_display = ["title"]
    #fields = ["property_name", "location_address"]

class publicationAdmin(admin.ModelAdmin):
    search_fields = ["title", "staff_id", "journal"]
    list_filter = ["department", "visibility"]
    readonly_fields = ['id', ]
    #fields = ["property_name", "location_address"]
    # list_display = ["user_email", "property_name", "number_of_rooms", "property_price"]

# Register your models here.
admin.site.register(message)
admin.site.register(student)
admin.site.register(staff)
admin.site.register(publication)
admin.site.register(book)
admin.site.register(lecture_note)
admin.site.register(leasing)
admin.site.register(reading_list)
admin.site.register(gen_login)