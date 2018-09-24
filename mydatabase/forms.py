from django import forms



class EmailForm(forms.Form):
    name = forms.CharField(
            label='',
            widget=forms.TextInput(attrs={'class': 'name_email', 'placeholder': 'Imię ...'})
    )

    description = forms.CharField(label='', widget=forms.Textarea(attrs={
            'class': 'email_form_description',
            'placeholder': 'Opis ...'
    }))

    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'email_email', 'placeholder': 'Poczta ...'}))



class SendForm(forms.Form):
    title = forms.CharField(
            label='',
            widget=forms.TextInput(attrs={
                'class' : 'sendformtitle',
                'placeholder' : 'Title ...'})
    )

    body = forms.CharField(
            label='',
            widget=forms.Textarea(attrs={
                'class' : 'sendformbody',
                'placeholder' : 'Body ...'})
    )
