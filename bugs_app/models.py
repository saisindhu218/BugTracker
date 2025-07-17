from django.db import models
from projects_app.models import Project  # ✅ Make sure this import is correct

class Bug(models.Model):
    PRIORITY_CHOICES = [
        ('LO', 'Low'),
        ('MD', 'Medium'),
        ('HI', 'High')
    ]

    STATE_CHOICES = [
        ('RE', 'Resolved'),
        ('UN', 'Unresolved')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Renamed for clarity
    name = models.CharField(max_length=50)
    desc = models.TextField()
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)

    def __str__(self):  # ✅ Fixed method name
        return self.name