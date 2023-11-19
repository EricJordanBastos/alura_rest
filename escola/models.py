from django.db import models

# Create your models here.

class aluno(models.Model):
    nome=models.CharField(max_length=30)
    rg=models.CharField(max_length=9)
    cpf=models.CharField(max_length=11)
    data_nascimento=models.DateField()
    
    
    def __str__(self):
        return self.nome


class curso(models.Model):
    NIVEL=(('B','Básico'),('I','Intermediário'),('A','Avançado'))
    
    codigo=models.CharField(max_length=10)
    descricao=models.CharField(max_length=100)
    nivel=models.CharField(max_length=1,choices=NIVEL,null=False,blank=False,default='B')

    def __str__(self):
        return self.descricao