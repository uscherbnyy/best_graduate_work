from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField

from ToDo.models import Task


class TaskForm(ModelForm):
    created_by = ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['created_by','title', 'description', 'status', 'completed', 'completed_at',
                  'deleted_at', 'deleted', 'category', 'priority']


