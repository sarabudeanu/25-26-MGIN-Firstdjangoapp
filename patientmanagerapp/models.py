from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    birthday = models.DateTimeField()
    svnr = models.CharField(max_length=11)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
class Practitioner(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=32)
    