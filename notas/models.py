from django.core.urlresolvers import reverse
from django.db import models

class Turma(models.Model):
	desc_turma = models.CharField(max_length=30)
	def __str__(self):
		return self.desc_turma

class Prova(models.Model):
	data = models.DateTimeField('data')
	valor = models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return self.valor

class Aluno(models.Model):
	nome = models.CharField(max_length=45)
	turma = models.ForeignKey(Turma)
	provas = models.ManyToManyField(Prova)
	def __str__(self):
		return self.nome
	def get_absolute_url(self):
		return reverse('notas:aluno_detail', kwargs={'pk': self.pk})
