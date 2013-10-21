from django.http import HttpResponse, Http404
from django.shortcuts import render
from forum.models import Forum, Thread, Post

def index(request):
	try:
		output = Forum.objects.all()
	except Forum.DoesNotExist:
		raise Http404

	return render(request, 'forum/index.html', {"output":output})

def forum(request, forum_id):
	forum = Forum.objects.get(id=forum_id)
	list_of_threads = Thread.objects.filter(forum_id=forum_id)

	return render(request, 'forum/forum.html', {"forum":forum, "list_of_threads":list_of_threads})

def thread(request, forum_id,thread_id):
	forum = Forum.objects.get(id=forum_id)
	thread = Thread.objects.filter(id=thread_id)
	list_of_posts = Post.objects.filter(thread_id=thread_id)

	return render(request, 'forum/thread.html', {"forum":forum,"thread":thread, "list_of_posts":list_of_posts})

def post(request, forum_id, thread_id, post_id):
	return HttpResponse("You're looking at Post %s from Thread %s" % (post_id, thread_id))