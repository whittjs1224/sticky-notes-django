"""Tests for the notes app: the Note model and the CRUD views."""

from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTest(TestCase):
    """Tests for the Note model."""

    def test_str_returns_title(self):
        """A note shows its title in the admin site and templates."""
        note = Note.objects.create(title="Shopping", content="Milk")
        self.assertEqual(str(note), "Shopping")

    def test_color_defaults_to_yellow(self):
        """A note saved without a color is yellow."""
        note = Note.objects.create(title="Plain", content="No color")
        self.assertEqual(note.color, "yellow")


class NoteViewTests(TestCase):
    """Tests for the list, detail, create, update and delete views."""

    def setUp(self):
        """Create one note that each test can use."""
        self.note = Note.objects.create(
            title="First note", content="Hello", color="pink"
        )

    def test_list_shows_notes(self):
        """The home page lists every note."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First note")

    def test_detail_shows_note(self):
        """The detail page shows the note's content."""
        url = reverse("note_detail", args=[self.note.pk])
        response = self.client.get(url)
        self.assertContains(response, "Hello")

    def test_detail_missing_note_returns_404(self):
        """Asking for a note that does not exist gives "Not found"."""
        response = self.client.get(reverse("note_detail", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_create_saves_note_and_redirects(self):
        """A valid form saves a new note and returns to the list."""
        data = {"title": "New", "content": "Text", "color": "blue"}
        response = self.client.post(reverse("note_create"), data)
        self.assertRedirects(response, reverse("note_list"))
        self.assertTrue(Note.objects.filter(title="New").exists())

    def test_create_with_missing_title_saves_nothing(self):
        """An invalid form is shown again and nothing is saved."""
        data = {"title": "", "content": "Text", "color": "blue"}
        response = self.client.post(reverse("note_create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 1)

    def test_update_changes_note(self):
        """Editing a note saves the new values."""
        url = reverse("note_update", args=[self.note.pk])
        data = {"title": "Changed", "content": "Hello", "color": "green"}
        response = self.client.post(url, data)
        self.assertRedirects(
            response, reverse("note_detail", args=[self.note.pk])
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Changed")
        self.assertEqual(self.note.color, "green")

    def test_delete_get_does_not_delete(self):
        """Opening the delete page only asks for confirmation."""
        url = reverse("note_delete", args=[self.note.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Note.objects.filter(pk=self.note.pk).exists())

    def test_delete_post_removes_note(self):
        """Confirming the delete removes the note."""
        url = reverse("note_delete", args=[self.note.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse("note_list"))
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
