from rest_framework import viewsets
from escola.serializer import AlunoSerializer, CursoSerializer,MatriculaSerializer
from escola.models import aluno, curso, matricula

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos Alunos e Alunas"""
    queryset=aluno.objects.all()
    serializer_class=AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset=curso.objects.all()
    serializer_class=CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset=matricula.objects.all()
    serializer_class=MatriculaSerializer