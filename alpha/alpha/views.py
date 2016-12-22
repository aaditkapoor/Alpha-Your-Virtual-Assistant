from django.shortcuts import render_to_response
from . import alpha
import re
from .models import AlphaKnowledge, AlphaReminder
from django.http import HttpResponse

def home(request):
	return render_to_response("index.html")


def alpha_request(request):
	query = request.GET.get("query","")
	query = query.lower()
	reminder = ""
	if query == "weather":
		#weather_gather_data()
		pass
	elif re.match(r'^remind me',query):
		reminder = alpha.check_reminder_request(query)
		if reminder:
			AlphaReminder.objects.create(reminder=reminder)
			return HttpResponse(reminder)
		else:
			return HttpResponse("Wrong format!")
	else:
		if AlphaKnowledge.objects.get(question=query).exists():
			print AlphaKnowledge.objects.get(question=query).response
		else:
			return render_to_response("teach.html",{"query":query})




