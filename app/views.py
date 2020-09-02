from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Video
from django.views.decorators.csrf import csrf_exempt
from .forms import VideoForm  # to include the form
from django.views import generic


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        # print('data was posted')
        # return HttpResponse('Hello')
        # print (f'data -- {request.POST}')
        return HttpResponse(f'data -- {request.POST.get("mymessage")}')
    genres = Genre.objects.all()
    videos = Video.objects.all()
    myvideoform = VideoForm()
    context = {
        'videos': videos,
        'genres': genres,
        'myform': myvideoform
    }
    # return HttpResponse('Welcome to Crappy Netflix')
    return render(request, 'app/index.html', context)

def search(request):
    if request.method == 'POST':
        return HttpResponse(f'data -- {request.POST.get(request)}')
    else:
        return HttpResponse('no data searched!')

class VideoListView(generic.ListView):
    model= Video
    context_object_name = 'videos'

class VideoDetailView(generic.DeleteView):
    model=Video
