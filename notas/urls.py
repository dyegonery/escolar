from django.conf.urls import patterns, url
from notas import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^alunos/$', views.AlunoIndex.as_view(), name="alunos"),
	url(r'^alunos/create$', views.AlunoCreate.as_view(), name="aluno_create"),
	url(r'^alunos/(?P<pk>\d+)$', views.AlunoDetail.as_view(), name="aluno_detail"),
	url(r'^alunos/update/(?P<pk>\d+)$', views.AlunoUpdate.as_view(), name="aluno_update"),
)