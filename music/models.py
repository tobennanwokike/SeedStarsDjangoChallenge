from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
	fullName = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)

	def get_absolute_url(self):
		return reverse('music:list')

	def __str__(self):
		return self.fullName + ', ' + self.email
		
