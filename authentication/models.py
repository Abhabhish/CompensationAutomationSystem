from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('PIU', 'PIU'),
        ('Circle', 'Circle'),
        ('Zonal', 'Zonal'),
        ('Urrda', 'Urrda'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def is_piu(self):
        return self.role == 'PIU'

    def is_circle(self):
        return self.role == 'Circle'

    def is_zonal(self):
        return self.role == 'Zonal'

    def is_urrda(self):
        return self.role == 'Urrda'