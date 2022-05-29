from django.shortcuts import render
from .models import Photo
from django.http import Http404

# Create your views here.
def index(request):
    return render(request,'index.html')

def photo(request):
    try:
        photo = Photo.objects.all()
    except Photo.DoesNotExist:
        raise Http404()
    return render(request,'photo.html',{"photos":photo})




def photo_search(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    