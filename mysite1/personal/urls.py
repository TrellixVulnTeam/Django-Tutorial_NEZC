
from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$',views.index,name='perosnalindex'),
	url(r'^contact/',views.contact,name='contact'),
	               
				   
				   
]
