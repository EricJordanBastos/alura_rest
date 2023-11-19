from rest_framework import viewsets,generics
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadoSerializer
from escola.models import aluno, curso, matricula
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos Alunos e Alunas"""
    queryset=aluno.objects.all()
    serializer_class=AlunoSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset=curso.objects.all()
    serializer_class=CursoSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]    

class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset=matricula.objects.all()
    serializer_class=MatriculaSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno"""
    def get_queryset(self):
        queryset=matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class=ListaMatriculaAlunoSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset=matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class=ListaAlunosMatriculadoSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]