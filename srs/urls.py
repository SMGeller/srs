from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome_text, name="welcome"),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^create_account/', views.create_account, name="create_account"), 
	url(r'^login/', views.login),  
	url(r'^notefile_list', views.notefile_list, name='notefile_list'),
	url(r'^notefile/(?P<name>[-\w]+)/$', views.notefile_detail, name='notefile_detail'),
	url(r'^notecard_list/(?P<name>[-\w]+)/$', views.notecard_list, name='notecard_list'),  
	url(r'^notecard/(?P<pk>\d+)/$', views.notecard_detail, name='notecard_detail'),
	url(r'^create_notefile', views.notefile_new, name='create_notefile'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^about/$', views.about, name='about'),   
]