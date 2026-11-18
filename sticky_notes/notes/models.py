"""Database models for the notes app."""

from django.db import models


class Note(models.Model):
    """A sticky note with a title, some content and a color."""

    COLOR_CHOICES = [
        ("yellow", "Yellow"),
        ("pink", "Pink"),
        ("blue", "Blue"),
        ("green", "Green"),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    color = models.CharField(
        max_length=10, choices=COLOR_CHOICES, default="yellow"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        """Show the note's title in the admin site and templates."""
        return self.title
