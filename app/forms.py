from django.forms import ModelForm
from app.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'performer', 'status', 'label', 'description']
