from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from task_manager.mixin import CheckUserForDeleteMixin
from django.utils.translation import gettext as _


class IndexView(TemplateView):
    template_name = 'index.html'


class UsersList(ListView):
    model = get_user_model()
    template_name = 'users/users.html'
    context_object_name = 'users'


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('index')

    template_name = 'users/registration.html'
    success_message = _('User was successfully created')


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('index')
    success_message = _('Welcome to your profile')


class LogoutUser(LogoutView):
    template_name = 'users/logout.html'
    success_url = 'login/'


class EditUser(LoginRequiredMixin, CheckUserForDeleteMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/edit_user.html'
    fields = ['first_name', 'last_name', 'username', 'email']
    permission_denied_message = _('You do not have permission to modify another user.')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('users'))

    def get_success_url(self):
        return reverse('users')


class DeleteUser(LoginRequiredMixin, CheckUserForDeleteMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete_user.html'
    permission_denied_message = _('You do not have permission to modify another user')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('users'))

    def get_success_url(self):
        return reverse('users')