from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact  # модель Contact для ContactForm


# Форма регистрации пользователя
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


# Форма обратной связи
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if 'спасибо' not in subject.lower():
            raise forms.ValidationError('Вы обязательно должны нас поблагодарить!')
        return subject
