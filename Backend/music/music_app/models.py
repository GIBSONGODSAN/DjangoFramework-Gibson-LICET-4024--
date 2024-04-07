from django.db import models

# Create your models here.
class UserDetails(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    profileName = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    marketingCheckbox = models.BooleanField() 

    def __str__(self):
        return self.email