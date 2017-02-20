from django.db import models
from django.core.urlresolvers import reverse

class PostManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(titulo__icontains=query) | \
			models.Q(texto__icontains=query)
	)

class Post(models.Model):

	title = models.CharField('Titulo', max_length=100, blank=False)
	slug = models.SlugField('Slug')
	text = models.TextField('Texto', blank=False)
	date_post = models.DateField('Postado em', null=True, blank=False)
	image = models.ImageField(upload_to='blog/images', verbose_name='Imagem', null=True, blank=False)
	created_at = models.DateTimeField('Criado em', auto_now=False, auto_now_add=True, blank=False)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True, auto_now_add=False)

	objects = PostManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:details', kwargs={'slug': self.slug})

class Meta:
	ordering = ['-created_at']
