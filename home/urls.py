from django.urls import path
from . import views
app_name= 'pages'
urlpatterns = [
path('',views.available,name='available'),
path('confirmation/',views.thanks,name='confirmation'),

]
