from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_added", "lang")
    search_fields = ("title",)

# Register your models here.
admin.site.register(Book, BookAdmin)
