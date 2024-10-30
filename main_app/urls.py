
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
	# Detail (show page) shows one cat
	path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
	# CBV (class based views), must call the as_view() method
	path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
	# CBV (class based views) the param will always be pk by convention
	# pk = primary key = id
	path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
	path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add-feeding'),
	path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
	path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
	path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
	path('toys/', views.ToyList.as_view(), name='toy-index'),
	    #Existing urls above
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),

]
