
from django.urls import path
from . import views # import all the view functions in the view file,
# and attach them to the views object


# ALL of our routes our defined here for our main_app
urlpatterns = [
	# like '/' in express
	# an empty string is localhost:8000
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('cats/', views.cat_index, name='cat-index'),
]
