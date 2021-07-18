from django.conf.urls import url, include

from . import views
urlpatterns = [
<<<<<<< HEAD
    url(r'home/$',views.homepage),
=======
    url(r'^home/$',views.homepage),
>>>>>>> 9ea83b64a1cba3cbec7e280f8f7500266953389a
    url(r'^2021/about/$',views.about),
]