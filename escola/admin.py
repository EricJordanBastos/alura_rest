from django.contrib import admin
from escola.models import aluno, curso, matricula
# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display=('id','nome','rg','cpf','data_nascimento')
    list_display_links=('id','nome')
    search_fields=('nome',)
    list_per_page=20

admin.site.register(aluno, Alunos)

class Cursos (admin.ModelAdmin):
    list_display=('id','codigo','descricao')
    list_display_links=('id','codigo')
    search_fields=('codigo',)

admin.site.register(curso,Cursos)

class Matriculas(admin.ModelAdmin):
    list_display=('id','aluno','curso','periodo')
    list_display_links=('id',)

admin.site.register(matricula,Matriculas)