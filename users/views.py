from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm  # Убедись, что форма есть в forms.py

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')  # переадресуем на страницу логина после успешной регистрации

def user_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thank-you/')  # или reverse()
        return render(request, 'users/contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'users/contact.html', {'form': form})
