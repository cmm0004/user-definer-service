from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.user_detail)
]