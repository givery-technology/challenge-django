from django.conf.urls import include, url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Class Based urls
    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?:/(?P<offset>\d+))?(?:/(?P<limit>\d+))?$', views.UserList.as_view(), name='user-list'),
    url(r'^api/join$', views.UserCreate.as_view(), name='user-create'),
    url(r'^api/login/$', views.UserDetail.as_view(), name='login'),
    url(r'^api/logout/$', views.UserDetail.as_view(), name='logout'),
    url(r'^api/users/(?P<pk>[\d]+)/$', views.UserDetail.as_view(), name='show-user'),
    url(r'^api/user/following/(?P<pk>[\d]+)/$', views.Follow.as_view(), name='follow'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
