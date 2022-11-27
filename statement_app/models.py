from django.db import models
from django.contrib.auth.models import User


class Statements(models.Model):
    objects = models.Model
    user_added_statement = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    client_inn = models.IntegerField()
    client_company_name = models.CharField(max_length=120)
    client_device_number = models.CharField(max_length=60)
    client_modul_number = models.CharField(max_length=60)
    client_number = models.CharField(max_length=40)
    client_address = models.CharField(max_length=120)
    client_single_window_statement = models.ImageField(upload_to='media', null=True, blank=True)
    client_statement = models.ImageField(upload_to='media', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    client_statement_added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_company_name
