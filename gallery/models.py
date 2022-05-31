from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    phone_number=models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()



    class Meta:
        ordering = ['first_name']
        
class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    
    # @classmethod
    # def search_by_name(cls,search_term):
    #     photos = cls.objects.filter(name__icontains=search_term)
    #     return photos


   

class Photo(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    date_posted=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo_url=models.CharField(max_length=200)
    photo_image = models.ImageField(upload_to = 'photo/',blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title

    def save_photo(self):
        self.save()


    def delete_photo(self):
        self.delete()

    @classmethod
    def update_photo(cls, id, value):
        cls.objects.filter(id=id).update(photo_image=value)

    @classmethod
    def filter_by_location(cls, location):
        photo_location = Photo.objects.filter(location__name=location).all()
        return photo_location

    @classmethod
    def search_by_category(cls, search_term):
        photos = cls.objects.filter(category__name__icontains=search_term)
        return photos

    # @classmethod
    # def filter_by_category(cls, category):
    #     photo_category = Photo.objects.filter(category__name=category).all()
    #     return photo_category

    # @classmethod
    # def search_by_title(cls,search_term):
    #     photos = cls.objects.filter(title__icontains=search_term)
    #     return photos



    
