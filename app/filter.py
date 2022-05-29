from django import forms
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from app.models import Task, Label
from django.utils.translation import gettext as _


class TaskFilter(FilterSet):
    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        label=_('labels')
    )
    self_tasks = BooleanFilter(
        widget=forms.CheckboxInput,
        field_name='author',
        method='filter_self_task',
        label=_('show my tasks')
    )

    def filter_self_task(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'author', 'label', 'self_tasks']
