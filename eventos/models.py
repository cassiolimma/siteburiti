from django.db import models

class EventoManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(title__icontains=query) | \
			models.Q(text__icontains=query)
	)

class Evento(models.Model):

	title = models.CharField('Titulo', max_length=100, blank=False)
	slug = models.SlugField('Slug')
	text = models.TextField('Descrição', blank=False)
	date_evento = models.DateField('Data do evento', null=True, blank=False)
	created_at = models.DateTimeField('Criado em', auto_now=False, auto_now_add=True, blank=False)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True, auto_now_add=False)

	objects = EventoManager()

	def __str__(self):
		return self.title

class Meta:
	ordering = ['-created_at']
			