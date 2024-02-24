from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cadastro(models.Model):
    Nome = models.CharField(max_length=100)
    Idade = models.CharField(max_length=3)
    Telefone = models.CharField(max_length=16)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

    class Metas:
        db_table = 'Cadastro'

    def __str__(self):
        return self.Nome

