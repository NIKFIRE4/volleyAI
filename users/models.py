from django.db import models
from django.contrib.auth.hashers import make_password

class Users(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, default='-')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
   




# Create your models here.
