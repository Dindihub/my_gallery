from django.shortcuts import render
from .models import Project
from django.http import Http404

# Create your views here.
def index(request):
    return render(request,'index.html')

# def photo(request):
#     try:
#         photo = Photo.objects.all()
#     except Photo.DoesNotExist:
#         raise Http404()
#     return render(request,'photo.html',{"photos":photo})
    