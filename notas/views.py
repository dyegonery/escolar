from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from notas.models import Prova, Aluno

def index(request):
	return render(request, 'notas/index.html')

class AlunoIndex(generic.ListView):
	model = Aluno
	template_name = 'notas/aluno_index.html'
	context_object_name = 'all_alunos'

class AlunoCreate(generic.CreateView):
	model = Aluno
	fields = ['nome', 'turma']

class AlunoUpdate(generic.UpdateView):
	model = Aluno
	fields = ['nome', 'turma']

class AlunoDetail(generic.DetailView):
	model = Aluno
	template_name = 'notas/aluno_detail.html'