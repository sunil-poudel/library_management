from django.contrib import admin
from notes.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "plan")

# Register your models here.
admin.site.register(Note, NoteAdmin)