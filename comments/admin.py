from django.contrib import admin
from comments.models import Comment
from books.models import Book

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "comments")
    search_fields = ("books__title", "comments", "books__author")
    #please look above line, book__title allows us to
    #search those books whose comments we forgot but title
    #we know

# Register your models here.
admin.site.register(Comment, CommentAdmin)
