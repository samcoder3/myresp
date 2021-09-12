from django.urls import path 
from .views import index,contact,about,PostList,Stuff,Addcomments






urlpatterns=[

	path('',index, name="index"),
	path('PostList/',PostList.as_view(), name='PostList'),
	path('contact/',contact, name='contact'),
	path('about/',about, name='about'),
	path('stuff/',Stuff, name='Stuff'),
	path('<int:pk>/comment/',Addcomments.as_view(), name='Addcomments'),

]