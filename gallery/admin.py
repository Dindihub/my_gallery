from django.contrib import admin
from .models import User,Photo,Category,Location

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal =('photo',)

admin.site.register(User)
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Location)


