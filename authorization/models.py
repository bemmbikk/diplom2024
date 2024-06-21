from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True)
    gender = models.CharField(max_length=10, choices=[('М', 'Мужской'), ('Ж', 'Женский')], blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
