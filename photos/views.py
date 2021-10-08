from django.shortcuts import render
from .models import Category,Photo,Location

# Create your views here.

def gallery(request):
    location = request.GET.get('location')

    if location ==  None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(location__name = location)



    categories = Category.objects.all()
    locations = Location.objects.all()

    return render(request,'photos/gallery.html', {"categories" : categories,"photos" : photos,"locations" : locations})

def viewPhoto(request,pk):
    photo = Photo.objects.get(id = pk)


    return render(request,'photos/photo.html', {"photo" : photo})
    
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_articles = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"categories": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})  