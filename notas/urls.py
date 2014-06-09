from django.conf.urls import patterns, url
from notas import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^alunos/$', views.AlunoIndex.as_view(), name="alunos"),
	url(r'^alunos/create$', views.AlunoCreate.as_view(), name="aluno_create"),
	url(r'^alunos/(?P<pk>\d+)$', views.AlunoDetail.as_view(), name="aluno_detail"),
	url(r'^alunos/update/(?P<pk>\d+)$', views.AlunoUpdate.as_view(), name="aluno_update"),
	url(r'^alunos/delete/(?P<id>\d+)$', views.AlunoDelete, name="aluno_delete"),
	url(r'^provas/$', views.ProvaIndex.as_view(), name="provas"),
	url(r'^provas/create$', views.ProvaCreate.as_view(), name="prova_create"),
	url(r'^provas/(?P<pk>\d+)$', views.ProvaDetail.as_view(), name="prova_detail"),
	url(r'^provas/update/(?P<pk>\d+)$', views.ProvaUpdate.as_view(), name="prova_update"),
	url(r'^provas/delete/(?P<id>\d+)$', views.ProvaDelete, name="prova_delete"),
	url(r'^turmas/$', views.TurmaIndex.as_view(), name="turmas"),
	url(r'^turmas/create$', views.TurmaCreate.as_view(), name="turma_create"),
	url(r'^turmas/(?P<pk>\d+)$', views.TurmaDetail.as_view(), name="turma_detail"),
	url(r'^turmas/update/(?P<pk>\d+)$', views.TurmaUpdate.as_view(), name="turma_update"),
	url(r'^turmas/delete/(?P<id>\d+)$', views.TurmaDelete, name="turma_delete"),
)
