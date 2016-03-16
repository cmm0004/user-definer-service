from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^twitterusers/$', views.TwitterUserList.as_view()),
    url(r'^twitterusers/(?P<user_id>[0-9]+)/$', views.TwitterUserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)