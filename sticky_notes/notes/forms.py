"""Forms for the notes app."""

from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and editing a note, built from the Note model."""

    class Meta:
        model = Note
        fields = ["title", "content", "color"]
        widgets = {
            "title": forms.TelInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "rows": 6}
            ),
            "color": forms.Select(attrs={"class": "form-select"}),
        }
