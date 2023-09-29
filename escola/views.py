from django.http import JsonResponse

def alunos(request):
    if request.method =='GET':
        dicionario={'id':1,'nome':'Eric'}
    return JsonResponse(dicionario)
# Create your views here.
