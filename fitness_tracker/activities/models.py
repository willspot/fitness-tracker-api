from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('RUNNING', 'Running'),
        ('CYCLING', 'Cycling'),
        ('WEIGHTLIFTING', 'Weightlifting'),
        ('SWIMMING', 'Swimming'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration = models.PositiveIntegerField()  # in minutes
    distance = models.FloatField()  # in km or miles
    calories_burned = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} by {self.user.username} on {self.date}"
