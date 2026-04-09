from django import forms
from .models import Task


INPUT_CLASS = (
    'w-full px-4 py-2.5 rounded-lg bg-white border border-gray-200 '
    'text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 '
    'focus:ring-violet-400 focus:border-transparent transition-all duration-200 text-sm'
)


class TaskForm(forms.ModelForm):
    """Form for creating and updating tasks."""

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'What needs to be done?',
                'class': INPUT_CLASS,
                'id': 'task-title-input',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Add a description (optional)',
                'rows': 2,
                'class': INPUT_CLASS + ' resize-none',
                'id': 'task-description-input',
            }),
            'priority': forms.Select(attrs={
                'class': INPUT_CLASS + ' appearance-none cursor-pointer',
                'id': 'task-priority-input',
            }),
            'deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': INPUT_CLASS + ' cursor-pointer',
                'id': 'task-deadline-input',
            }, format='%Y-%m-%dT%H:%M'),
        }

