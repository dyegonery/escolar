from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
import json

from notas.models import Prova, Aluno, Turma

def index(request):
	return render(request, 'notas/index.html')

# CRUD DE ALUNOS
class AlunoIndex(generic.ListView):
	model = Aluno
	template_name = 'notas/aluno_index.html'
	context_object_name = 'all_alunos'

class AlunoCreate(generic.CreateView):
	model = Aluno
	fields = ['nome', 'turma', 'provas']

class AlunoUpdate(generic.UpdateView):
	model = Aluno
	fields = ['nome', 'turma', 'provas']

class AlunoDetail(generic.DetailView):
	model = Aluno
	template_name = 'notas/aluno_detail.html'

def AlunoDelete(request, id):
	aluno = Aluno.objects.get(pk=id).delete()
	# Retorna "success" em json para requisicao ajax
	response = {'success': True}
	return HttpResponse(json.dumps(response), content_type='application/json')

# CRUD DE PROVAS
class ProvaIndex(generic.ListView):
	model = Prova
	template_name = 'notas/prova_index.html'
	context_object_name = 'all_provas'

class ProvaCreate(generic.CreateView):
	model = Prova
	fields = ['data', 'valor', 'turma']

class ProvaUpdate(generic.UpdateView):
	model = Prova
	fields = ['data', 'valor', 'turma']

class ProvaDetail(generic.DetailView):
	model = Prova
	template_name = 'notas/prova_detail.html'

def ProvaDelete(request, id):
	prova = Prova.objects.get(pk=id).delete()
	# Retorna "success" em json para requisicao ajax
	response = {'success': True}
	return HttpResponse(json.dumps(response), content_type='application/json')

# CRUD DE TURMAS
class TurmaIndex(generic.ListView):
	model = Turma
	template_name = 'notas/turma_index.html'
	context_object_name = 'all_turmas'

class TurmaCreate(generic.CreateView):
	model = Turma
	fields = ['desc_turma']

class TurmaUpdate(generic.UpdateView):
	model = Turma
	fields = ['desc_turma']

class TurmaDetail(generic.DetailView):
	model = Turma
	template_name = 'notas/turma_detail.html'

def TurmaDelete(request, id):
	turma = Turma.objects.get(pk=id).delete()
	# Retorna "success" em json para requisicao ajax
	response = {'success': True}
	return HttpResponse(json.dumps(response), content_type='application/json')
