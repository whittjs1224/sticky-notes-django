"""Views for the notes app: list, view, create, update and delete notes."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Show every note, most recently updated first."""
    notes = Note.objects.all()
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    """Show one note, or a "Not found" page if it does not exist."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """Show an empty form (GET), or save a new note (POST)."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """Show a form filled in with the note (GET), or save changes (POST)."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html",
                  {"form": form, "note": note})


def note_delete(request, pk):
    """Ask for confirmation (GET); delete the note only when confirmed."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})
