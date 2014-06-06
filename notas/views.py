from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from notas.models import Prova, Aluno

class IndexView(generic.ListView):
	template_name = 'notas/index.html'
	context_object_name = 'all_provas'
	def get_queryset(self):
		return Prova.objects.order_by('-data')