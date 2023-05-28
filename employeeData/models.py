from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)
    department = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
