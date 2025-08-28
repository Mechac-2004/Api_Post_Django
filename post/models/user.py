from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128) 
    
#     ROLE_CHOICES = (
#         ('superadmin', 'Super Admin'),
#         ('posteur', 'Posteur'),
#     )
#     role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='posteur')
    
#     is_active = models.BooleanField(default=False)
#     otp_code = models.CharField(max_length=6, blank=True, null=True)
#     otp_created_at = models.DateTimeField(null=True, blank=True)
    
#     def __str__(self):
#         return self.email

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('posteur', 'Posteur'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='posteur')
    
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.email