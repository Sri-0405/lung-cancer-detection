from django.db import models

# Create your models here.
from django.db import models

class XrayCTImage(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=gender_choices)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
