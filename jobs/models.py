from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company =models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    url = models.URLField(unique=True)
    source = models.CharField(max_length=100)
    date_posted = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"