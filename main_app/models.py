from django.db import models

from django.urls import reverse
# Create your models here.

# Add the Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})


class Cat(models.Model):
	name= models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()
	# Many to Many Relationship
	# this creates the join table for you!
	toys = models.ManyToManyField(Toy)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# redirecting to cat-detail page after a POST
		# looking at the urls.py path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
		return reverse("cat-detail", kwargs={"cat_id": self.id})


MEALS = (
	('B', 'Breakfast'),
	('L', 'Lunch'),
	('D', 'Dinner'),
)

class Feeding(models.Model):
	date = models.DateField('Feeding Date')
	meal = models.CharField(
			max_length=1,
			# choicess, for a select menu (on a form)
			choices=MEALS,
			# default value for the meal will be 'B'
			default=MEALS[0][0]
			)
	# create a cat_id column for our 1 Cat has many Feedings, Feeding belongs to a cat
	# Foriegn Key always goes on the many side!
	cat = models.ForeignKey(Cat, on_delete=models.CASCADE)# if you delete a cat, delete the associated feedings

	def __str__(self):
		# get_<field_name>_display() is a magic method
		# to get the human readable value for your the choice
		# so "B" becomes Breakfast when the Feeding is printed!
		return f"{self.get_meal_display()} on {self.date}"



