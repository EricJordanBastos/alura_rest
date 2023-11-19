from rest_framework import viewsets
from serializer import AlunoSerializer, CursoSerializer
from models import aluno, curso

class AlunoViewSet(viewsets.ModelViewSet):
    """Importa todos Alunos e Alunas"""
    queryset=aluno.objects.all()
    serializer_class=AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """Importa todos os Cursos"""
    queryset=curso.objects.all()
    serializer_class=CursoSerializer
