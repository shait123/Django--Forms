from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class Review(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
