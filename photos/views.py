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
