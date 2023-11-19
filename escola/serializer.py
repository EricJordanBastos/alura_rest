from rest_framework import serializers
from escola.models import aluno, curso, matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=aluno
        fields='__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=curso
        fields='__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model=matricula
        # fields='__all__'
        exclude=['']