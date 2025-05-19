# core/models.py
from django.db import models
from django.contrib.auth.models import User

class PrintModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=255)
    stl_file = models.FileField(upload_to='stl_files/')
    material = models.CharField(max_length=100)
    infill_percentage = models.IntegerField()
    layer_height = models.DecimalField(max_digits=5, decimal_places=2)  # Ensure this fits SQL Server precision rules
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.model_name} - {self.user.username}"
