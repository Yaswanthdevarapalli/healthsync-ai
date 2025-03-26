from django.db import models

class HealthData(models.Model):
    user_id = models.CharField(max_length=100)
    heart_rate = models.IntegerField()
    sleep_hours = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.timestamp}"