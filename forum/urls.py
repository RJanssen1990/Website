from django.conf.urls import patterns, include, url
from forum import views


urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^(?P<forum_id>\d+)/$', views.forum, name="forum"),
	url(r'^(?P<forum_id>\d+)/thread/(?P<thread_id>\d+)/$', views.thread, name="thread"),
	url(r'^(?P<forum_id>\d+)/thread/(?P<thread_id>\d+)/Post/(?P<post_id>\d+)/$', views.post, name='post'),
)