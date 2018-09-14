
from django.urls import path
from . import Views
urlpatterns = [
    path('', Views.homepage, name='home' ),
    path('count/', Views.count , name='count'),
    path('about/', Views.aboutpage)



]
