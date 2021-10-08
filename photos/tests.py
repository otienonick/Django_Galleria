from django.test import TestCase
from .models import Photo,Category,Location
# Create your tests here.

class LocationTestClass(TestCase):

    def setUp(self):
        self.new_location = Location(name = 'test_name')
        self.new_location.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))     

class CategoryTestClass(TestCase):

    def setUp(self):
        self.new_category = Category(name = 'test_name')
        self.new_category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))   

class PhotoTestClass(TestCase):
        def setUp(self):

            self.new_location = Location(name = 'test_name')
            self.new_location.save()

            self.new_category = Category(name = 'test_name')
            self.new_category.save()

            self.new_image = Photo(location = self.new_location,category = self.new_category,name ='test_name',description = 'test_description' )

        def test_instance(self):
            self.assertTrue(isinstance(self.new_image,Photo))   

        def test_save_method(self):
            self.new_image.save_image()
            images = Photo.objects.all()
            self.assertTrue(len(images) > 0)    

        def tearDown(self):
            Photo.objects.all().delete()
            Category.objects.all().delete()
            Location.objects.all().delete()

        def test_delete_method(self):
            self.new_image.save_image()
            self.new_image.delete_image()
            images = Photo.objects.all()
            self.assertTrue(len(images) == 0)    

        def test_update_method(self):
            self.new_image.save_image()
            self.new_image.update_image()
            images = Photo.objects.all()
            self.assertTrue(len(images) > 0) 

        def test_get_image_by_id(self):
            id = Photo.get_image_by_id()
            self.assertTrue(len(id) == 0)    


        def test_filter_by_location(self):
            location = Photo.filter_by_location()
            self.assertTrue(len(location) == 0)

        def test_search_image(self):
            category = Photo.search_image()
            self.assertTrue(len(category)  == 0)
                
            
                    

