from django.urls import re_path as url,path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='home'),
    path('photo/',views.photo,name='gallery'),
    path('search/', views.photo_search, name='photo_search'),

    # path ('search/<int:projectid>/',views.project_search,name ='projects')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)