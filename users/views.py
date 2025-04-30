from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from .forms import UserRegisterForm, UserLoginForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        send_mail(
            subject='Добро пожаловать!',
            message=f'Привет, {user.email}! Спасибо за регистрацию.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return response

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')
