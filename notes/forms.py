from django import forms
from .models import Note

class UpdateNoteForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)


    def clean_title(self):
        data = self.cleaned_data['title']
        if not data:
            raise ValidationError('Title is empty')

        return data

    def clean_content(self):
        data = self.cleaned_data['content']
        if not data:
            raise ValidationError('Content is empty')

        return data


