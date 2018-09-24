from django import forms


class NoteForm(forms.Form):
    title = forms.CharField(label="", widget= forms.TextInput(attrs={
        'class': 'note_form_title',
        'placeholder': 'Nagłówek ...'
    }))

    description = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'note_form_description',
        'placeholder': 'Opis ...'
    }))
