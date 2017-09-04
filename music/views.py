from .models import User
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = "all_users"

	def get_queryset(self):
		return User.objects.all()

class ListView(generic.ListView):
	template_name = 'music/list.html'
	context_object_name = "all_users"

	def get_queryset(self):
		return User.objects.all()

class UserCreate(CreateView):
	model = User
	fields = ['fullName', 'email']

class UserUpdate(UpdateView):
	model = User
	fields = ['fullName', 'email']

