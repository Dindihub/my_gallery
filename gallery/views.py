from django.shortcuts import render
from .models import Photo,Category
from django.http import Http404

# Create your views here.
def index(request,pk):
    photo=Photo.objects.get(pk=pk)
    return render(request,'index.html',{"photos":photo})

def photo(request):
    try:
        photo = Photo.objects.all()
    except Photo.DoesNotExist:
        raise Http404()
    return render(request,'index.html',{"photos":photo})




def category_search(request):

    if 'category_search' in request.GET and request.GET["category_search"]:
        search_term = request.GET.get("category_search")
        searched_category = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_category": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


# def category_search(request):

#     if 'category' in request.GET and request.GET["category"]:
#         search_term = request.GET.get("category")
#         searched_photos = Category.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'category.html',{"message":message,"categorys": searched_photos})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})
    