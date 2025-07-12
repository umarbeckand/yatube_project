
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm as CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')  # после регистрации отправим на логин

# Create your views here.
