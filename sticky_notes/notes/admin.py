"""Admin site settings for the notes app."""

from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """List notes in the admin site with their color and last update."""

    list_display = ("title", "color", "updated_at")
    search_fields = ("title", "content")
