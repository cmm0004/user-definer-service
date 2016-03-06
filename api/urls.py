from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)