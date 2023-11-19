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
        exclude=[]

class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso=serializers.ReadOnlyField(source='curso.descricao')
    periodo=serializers.SerializerMethodField()
    class Meta:
        model=matricula
        fields=['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadoSerializer(serializers.ModelSerializer):
    aluno_nome=serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model=matricula
        fields=['aluno_nome']


