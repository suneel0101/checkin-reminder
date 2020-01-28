from django.utils import timezone
from twilio.rest import Client

from django.conf import settings
from .models import Ping


def send_sms(message):
	client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	client.messages.create(to=settings.TWILIO_TO, from_=settings.TWILIO_FROM, body=message)


def create_ping_and_send_sms(config):
	ping = Ping.objects.create(
		config=config,
		text=config.ping_text,
	)

	config.last_run_timestamp = timezone.now()
	config.save()

	send_sms(ping.text)