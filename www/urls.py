from django.conf.urls import url

from www import views

urlpatterns = [

    url(r'^home/$' , views.homePage),
    url(r'signup/$' ,views.signup)
]