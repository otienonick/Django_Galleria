from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Photo(models.Model):
    location = models.ForeignKey(Location,on_delete = models.SET_NULL,null=True)
    category = models.ForeignKey(Category,on_delete = models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'articles/',null = False)
    description = models.TextField()


    def __str__(self):
        return self.description

    def save_image(self):
        self.save() 

    def delete_image(self):
        self.delete()  

    def  update_image(self):
        self.save()  

    @classmethod
    def filter_by_location(cls):
        locate = Location
        image = cls.objects.filter(location__name = locate)
        return image

    @classmethod
    def search_image(cls):
        search_term = Category
        photos = cls.objects.filter(category__name = search_term)   
        return photos   

    @classmethod
    def get_image_by_id(cls,id=None):
        photos = cls.objects.filter(id = id)   
        return photos         
   
           
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__name__icontains = search_term)   
        # We filter the model data using the __icontains query filter
        return photos            