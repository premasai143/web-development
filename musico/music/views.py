from django.shortcuts import render
from . import models

# Create your views here.

def music(request):
	if request.user.is_authenticated:
		movies=models.movielist.objects.all()
		return render(request,'music/home.html',{'movie_list':movies})
	else:
		return HttpResponse("you need to access to access")
def listsong(request,pk):
	movie=models.movielist.objects.get(pk=pk)
	return render(request,'music/list.html',{'album':movie})		
