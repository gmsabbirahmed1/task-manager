from django.db import models
from django.utils import timezone
from datetime import timedelta


class Task(models.Model):
    """A single task in the task manager."""

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def is_overdue(self):
        """True if the task has a deadline in the past and is not completed."""
        if self.deadline and not self.completed:
            return timezone.now() > self.deadline
        return False

    @property
    def is_due_soon(self):
        """True if the deadline is within the next 24 hours."""
        if self.deadline and not self.completed:
            now = timezone.now()
            return now < self.deadline <= now + timedelta(hours=24)
        return False

    @property
    def priority_color(self):
        """Return Tailwind color name for this priority level."""
        return {
            'low': 'emerald',
            'medium': 'amber',
            'high': 'red',
        }.get(self.priority, 'violet')
