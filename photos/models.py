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