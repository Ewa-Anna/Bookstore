from django.contrib import admin
from .models import Book, Category, Review


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "price",
    )
    list_filter = ("catid",)
    prepopulated_fields = {"slug": ("title", "author")}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "rating", "book", "created", "active")
    list_filter = ("active", "created")
    search_fields = ("user", "rating", "body")


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
