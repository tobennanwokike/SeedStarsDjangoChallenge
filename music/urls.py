from django.conf.urls import url
from . import views

app_name = 'music'
	
urlpatterns = [
	# /music/
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'list/$', views.ListView.as_view(), name='list'),

	# /music/71/
	url(r'add/$', views.UserCreate.as_view(), name='user-add'),
	url(r'user/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='user-update'),



]