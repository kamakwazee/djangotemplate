
from django.http import HttpResponse

def index(request):
	return HttpResponse("Automated Deployment <3")
