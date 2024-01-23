from django.contrib import admin
from job_application.models import Form


# Class which help to design admin panel interface
class FormAdmin(admin.ModelAdmin):
    # Show columns in admin panel
    list_display = ("first_name", "last_name", "email")
    # Columns for searching
    search_fields = ("first_name", "last_name", "email")
    # Filters
    list_filter = ("date", "occupation")
    # Order by
    ordering = ("first_name",)
    # Unchangeable
    readonly_fields = ("first_name", "last_name", "email")


admin.site.register(Form, FormAdmin)
