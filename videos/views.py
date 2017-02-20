from django.shortcuts import render
from .models import Video

def index(request):
	videos = Video.objects.all()
	template_name = 'videos/index.html'
	context = {
		'videos': videos
	}
	return render(request, template_name, context)