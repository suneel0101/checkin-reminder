import json
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Ping


def handle_sms_response(request):
	text = request.POST['Body']
	latest_ping = Ping.objects.order_by('-id')[0]
	latest_ping.response = text
	latest_ping.timestamp_responded = timezone.now()
	latest_ping.save()
	return HttpResponse('Saved!')
