from django.test import TestCase
from .models import User,Photo,Location,Category



class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.sandra= User(first_name = 'Sandra', last_name ='Dindi', email ='sandra@moringaschool.com',phone_number='55555555')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.sandra,User))

    def test_save_method(self):
        self.sandra.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(name='Travel')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class PhotoTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

        self.category = Category(name='Travel')
        self.category.save_category()

        self.user = User(first_name='Sandra')
        self.user.save_user()

        self.photo_test = Photo(id=1, title='photo', description='this is a photo',user=self.user, photo_image='image',photo_url='url', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.photo_test, Photo))

    def test_save_photo(self):
        self.photo_test.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)

    def test_delete_photo(self):
        self.photo_test.delete_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) == 0)

    def test_update_photo(self):
        self.photo_test.save_photo()
        self.photo_test.update_photo(self.photo_test.id, 'photos/test.jpg')
        changed_img = Photo.objects.filter(photo_image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_search_photo_by_location(self):
        self.photo_test.save_photo()
        found_photos = self.photo_test.filter_by_location(location='Nairobi')
        self.assertTrue(len(found_photos) == 1)

    def test_search_photo_by_category(self):
        self.photo_test.save_photo()
        found_photos = self.photo_test.filter_by_category(category='Travel')
        self.assertTrue(len(found_photos) == 1)


