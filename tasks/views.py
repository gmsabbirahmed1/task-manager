from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Task
from .forms import TaskForm


def task_list(request):
    """Display all tasks and handle new task creation."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('tasks:list')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    pending = total - completed
    overdue = sum(1 for t in tasks if t.is_overdue)

    context = {
        'form': form,
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending,
        'overdue': overdue,
        'now': timezone.now(),
    }
    return render(request, 'tasks/task_list.html', context)


def task_update(request, pk):
    """Edit an existing task."""
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks:list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})


def task_toggle(request, pk):
    """Toggle the completed status of a task."""
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    status = 'completed' if task.completed else 'reopened'
    messages.success(request, f'Task marked as {status}!')
    return redirect('tasks:list')


def task_delete(request, pk):
    """Delete a task permanently."""
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, 'Task deleted!')
    return redirect('tasks:list')
