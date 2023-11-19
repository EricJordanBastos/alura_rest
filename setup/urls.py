from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet,CursoViewSet,MatriculaViewSet, ListaMatriculasAluno,ListaAlunosMatriculados
from rest_framework import routers

router=routers.DefaultRouter()
router.register('alunos',AlunoViewSet,basename='Alunos')
router.register('cursos',CursoViewSet,basename='Cursos')
router.register('matricula',MatriculaViewSet,basename='Matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matricula/',ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matricula/',ListaAlunosMatriculados.as_view()),
]
