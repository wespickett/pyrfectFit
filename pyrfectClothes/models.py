from django.db import models

# Create your models here.
class MaleShirt(models.Model):
    arm_length = models.DecimalField(default=0.0,max_digits=5,decimal_places=2)
    neck_circumference = models.DecimalField(default=0.0,max_digits=5,decimal_places=2)
    shoulders_circumference = models.DecimalField(default=0.0,max_digits=5,decimal_places=2)
    arm_circumference_upper = models.DecimalField(default=0.0,max_digits=5,decimal_places=2)
    chest_circumference = models.DecimalField(default=0.0,max_digits=5,decimal_places=2)
    waist_circumference = models.DecimalField(default=0.0,max_digits=5,decimal_places=2)
