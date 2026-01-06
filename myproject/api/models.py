from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    STATUS = (
        ('a', 'Available'),
        ('o', 'Offline'),
        ('b', 'Break')
    )
    availability_status = models.CharField(
        max_length= 1,
        choices = STATUS,
        blank= True,
        default='a',
        help_text='is this mongopack available, offline, or he took a break',

    )
    def __str__(self):
        return self.title
