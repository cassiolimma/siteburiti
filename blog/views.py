from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post

def index(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 3)

	
	if request.GET.get('q'):
		posts = posts.filter(
			Q(title__icontains=posts) | \
			Q(text__icontains=posts)			
			).distinct()

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first pageuery.
		posts = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	
	template_name = 'blog/index.html'
	context = {
		'posts': posts
	}
	return render(request, template_name, context)


def details(request, slug):	
	post = get_object_or_404(Post, slug=slug)
	context = {
		'post': post
	}
	template_name = 'blog/details.html'
	return render(request, template_name, context)