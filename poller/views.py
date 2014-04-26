
from django.http import HttpResponse
from django.template import Context, loader
from poller.models import Poll

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	template = loader.get_template('poller/index.html')
	context = Context({
			'latest_poll_list': latest_poll_list,
		})
	return HttpResponse(template.render(context))

def detail(request, poll_id):
	return HttpResponse('You are looking at poll %s.' % poll_id)

def results(request, poll_id):
	return HttpResponse('You are looking at the results of poll %s.' % poll_id)

def vote(request, poll_id):
	return HttpResponse('You are voting on poll %s.' % poll_id)
