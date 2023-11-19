from rest_framework import serializers
from escola.models import Aluno, Curso

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Aluno
        fields=['nome','rg','cpf','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Curso
        fields='__all__'

