from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Video
from django.views.decorators.csrf import csrf_exempt

from .forms import VideoForm # to include the form

# Create your views here.
@csrf_exempt
def index(request):
    if request.method =='POST':
        #print('data was posted')
        #return HttpResponse('Hello')

        #print (f'data -- {request.POST}')

        return HttpResponse(f'data -- {request.POST.get("mymessage")}')
    genres = Genre.objects.all()
    video = Video.objects.first()
    myvideoform=VideoForm()

    #return HttpResponse('Welcome to Crappy Netflix')
    return render(request, 'index.html', {'video': video, 'genres': genres,'myform':myvideoform})