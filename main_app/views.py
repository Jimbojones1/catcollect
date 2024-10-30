from django.shortcuts import render, redirect
from .models import Cat, Toy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# res.send in node
from django.http import HttpResponse
# Create your views here.

from .forms import FeedingForm

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

# cat_id comes from the 
# the url route  path('cats/<int:cat_id>/', views
def cat_detail(request, cat_id): # like req.params
	# find the row in the db that matches the cat_id with
	# the row number
	cat_from_db = Cat.objects.get(id=cat_id)
	# respond with the template

	feeding_form = FeedingForm()# creating a form object to pass into 
	# our template
	return render(request, 'cats/detail.html', {'cat': cat_from_db, 'feeding_form': feeding_form})

# path('cats/<int:pk>/add_feeding/', views.add_feeding, name='add-feeding'),
# cat_id needs to match the url param ^^^^
def add_feeding(request, cat_id):
	# process the post request and create a feeding!
	form = FeedingForm(request.POST)# request.POST is like req.body
	# you're creating a form instance by filling out the form with 
	# the data from the request(form submission)
	# validate the form
	if form.is_valid():
		# don't save it until we add the cat_id 
		new_feeding = form.save(commit=False)
		# Makes an in memory representation of our new feeding row in psql
		new_feeding.cat_id = cat_id
		new_feeding.save()# adds the row to the feeding table
	# redirect to cat-detail page, (cat_id (left) is from the param name)

	# import redirect at the top
	return redirect('cat-detail', cat_id=cat_id)





# This expects a template in the format of 
# templates/<app_name>/<model_name>_form.html
# templates/main_app/cat_form.html
class CatUpdate(UpdateView):
	model = Cat
	# disallow the renaming of a cat by exluding the name field
	fields = ['breed', 'description', 'age']
	# GO to the models.py file for the Cat model
	# to see where the CatUpdate redirects to, after
	# a POST request


class CatDelete(DeleteView):
	model = Cat
	success_url = '/cats/'# refering to a url! in the urls.py!


# This expects a template in the format of 
# templates/<app_name>/<model_name>_form.html
# templates/main_app/cat_form.html
class CatCreate(CreateView):
	model = Cat
	fields = '__all__'
	# GO to the models.py file for the Cat model
	# to see where the CatCreate redirects to, after
	# a POST request

	# success_url = '/cats/'











## ======================================
# THIS IS ONLY FOR TODAY FRIDAY (FIRST DAY)
# We are creating a class, and instatiating some objects from 
# that class so we can simulate having some data, so we can pass it
# into the cats index
# We're doing this because we don't have a model yet!
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]
## ================================================================


def home(request):
	return 	render(request, 'home.html')


def about(request):
	
	# render looks inside of the templates 
	# folder automatically for your template files!
	return render(request, 'about.html')

def cat_index(request):
	# search psql cats table and get all the rows!
	cats = Cat.objects.all()



	# cats/index.html - is looking inside of the
	# templates folder
	# we make a folder for each resource,
	# in this case cats
	return render(request, 'cats/index.html', {'cats': cats})