from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, \
    CreateView, \
    DeleteView, \
    UpdateView, \
    DetailView, TemplateView
from django_filters.views import FilterView
from app.filter import TaskFilter
from app.forms import TaskForm, UserForm
from app.mixin import CheckUserForDeleteMixin
from app.models import Status, Task, Label
from django.utils.translation import gettext as _


class StatusList(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/create_stat.html'
    success_message = _('Status successfully created')

    def get_success_url(self):
        return reverse('statuses')


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/update_stat.html'
    success_message = _('Status successfully updated')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('statuses'))

    def get_success_url(self):
        return reverse('statuses')


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete_stat.html'
    success_message = _('Status successfully deleted')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('statuses'))

    def get_success_url(self):
        return reverse('statuses')

    def delete(self, request, *args, **kwargs):
        if self.get_object().status.all().exists():
            messages.error(
                self.request, _(
                    'Unable to delete status because it is in use'
                )
            )
            return redirect('statuses')
        messages.success(self.request, _('Status successfully deleted'))
        return super().delete(request, *args, **kwargs)


class TaskList(LoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'


class CreateTask(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_message = _('Task successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update_task.html'
    success_message = _('Task successfully updated')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('tasks'))

    def get_success_url(self):
        return reverse('tasks')


class DeleteTask(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_message = _('Task successfully deleted')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('tasks'))

    def get_success_url(self):
        return reverse('tasks')


class LabelList(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'

    def get_success_url(self):
        return reverse('labels')


class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'labels/create_label.html'
    success_message = _('Label successfully created')

    def get_success_url(self):
        return reverse('labels')


class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'labels/update_label.html'
    success_message = _('Label successfully updated')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('labels'))

    def get_success_url(self):
        return reverse('labels')


class DeleteLabel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete_label.html'
    success_message = _('Label successfully deleted')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('labels'))

    def get_success_url(self):
        return reverse('labels')


class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    # form_class = TaskForm
    template_name = 'tasks/detail_task.html'
    context_object_name = 'task'


class IndexView(TemplateView):
    template_name = 'index.html'


class UsersList(ListView):
    model = get_user_model()
    template_name = 'users/users.html'
    context_object_name = 'users'


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserForm

    def get_success_url(self):
        return reverse('login')

    template_name = 'users/registration.html'
    success_message = _('User was successfully created')


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('index')
    success_message = _('Welcome to your profile')


class LogoutUser(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)


class EditUser(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CheckUserForDeleteMixin,
    UpdateView
):
    model = get_user_model()
    template_name = 'users/edit_user.html'
    form_class = UserForm
    permission_denied_message = _(
        'You do not have permission to modify another user.'
    )
    success_message = _('User successfully updated')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('users'))

    def get_success_url(self):
        return reverse('users')


class DeleteUser(LoginRequiredMixin,
                 SuccessMessageMixin,
                 CheckUserForDeleteMixin,
                 DeleteView):
    model = get_user_model()
    template_name = 'users/delete_user.html'
    permission_denied_message = _(
        'You do not have permission to modify another user'
    )
    success_message = _('User was deleted successfully')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('users'))

    def get_success_url(self):
        return reverse('users')

    def delete(self, request, *args, **kwargs):
        if (
            self.get_object().executor.all().exists()
            or self.get_object().author.all().exists()
        ):
            messages.error(
                self.request,
                _('Unable to delete user because it is in use')
            )
            return redirect('users')
        messages.success(self.request, _('User deleted'))
        return super().delete(request, *args, **kwargs)
