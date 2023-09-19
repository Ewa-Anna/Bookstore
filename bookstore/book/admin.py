from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price",)
    prepopulated_fields = {"slug": ("title", "author")}

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
