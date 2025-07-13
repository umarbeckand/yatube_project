from django import forms
from django.contrib.auth.forms import UserCreationForm  # Импортируем правильную форму
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')  # Можешь добавить другие поля, если нужно

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Добавляем CSS класс к каждому полю
