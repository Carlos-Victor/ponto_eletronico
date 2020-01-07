from django.db import models

# Create your models here.

class Colaboradores(models.Model):
    colaborador = models.CharField("Colaborador", max_length=50)
    uid = models.CharField("UID do cartão RFID", max_length=8)

class Horarios(models.Model):
    colaborador = models.ForeignKey("Colaboradores", verbose_name=("Colaborador"), on_delete=models.CASCADE)
    data = models.DateField("Data", auto_now_add=True)
    horario = models.TimeField("Horario", auto_now_add=True)


