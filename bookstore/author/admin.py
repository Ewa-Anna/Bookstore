from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email", "created")
    list_filter = ("name", "surname", "created")
    prepopulated_fields = {"slug": ("name", "surname")}


admin.site.register(Author, AuthorAdmin)
