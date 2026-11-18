"""Top-level URL configuration for the sticky_notes project.

The admin site is at /admin/. Every other address is handed to the notes
app (see notes/urls.py).
"""


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("notes.urls")),
]
