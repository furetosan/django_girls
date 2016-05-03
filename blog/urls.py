from django.conf.urls import include, url
from . import views

# Create your URLs here.

urlpatterns = [
    url(r'^$',views.post_list)
    ]