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
        

class Photo(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    date_posted=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo_url=models.CharField(max_length=200)
    photo_image = models.ImageField(upload_to = 'photo/',blank=True)
    category = models.ManyToManyField('category')
    location = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.title

    def save_project(self):
        self.save()



    def delete_project(self):
        self.delete()

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name