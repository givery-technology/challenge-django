from django.conf.urls import include, url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Function Based urls
    # url(r'^api/users/$', views.users_list),
    # url(r'^api/users/(?P<pk>[\d]+)/$', views.users_detail),

    # Class Based urls
    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    # url(r'^api/users/join$', views.UserCreate.as_view()),
    url(r'^api/users/(?P<pk>[\d]+)/$', views.UserDetail.as_view()),
    url(r'^api/users/login/$', views.UserDetail.as_view(), name='login'),
    url(r'^api/users/logout/$', views.UserDetail.as_view(), name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)