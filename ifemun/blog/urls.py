from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^api$', views.Api.as_view(), name='blog_api'),
]
