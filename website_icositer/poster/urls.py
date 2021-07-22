from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^create/$',views.create, name='create'),
	url(r'^$',views.list, name='list'),
	url(r'^export_library_xls/$', views.export_library_xls),
]

app_name = 'poster'