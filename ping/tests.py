import datetime

from unittest.mock import Mock, patch
from freezegun import freeze_time
from model_bakery import baker

from django.core import management
from django.test import TestCase, override_settings

from .models import PingConfig, Ping


class ScheduledJobTestCase(TestCase):
	def tearDown(self):
		PingConfig.objects.all().delete()

	def setUp(self):
		# Create a pingconfig that needs a ping to be sent right now
		self.config_1 = baker.make(
			PingConfig, minutes_interval=20,
			last_run_timestamp=datetime.datetime(2020, 1, 28, 12, 12),
			ping_text="How much water did you drink?"
		)

		# Create a pingconfig that has a ping that does NOT to be sent right now
		self.config_2 = baker.make(
			PingConfig, minutes_interval=30,
			last_run_timestamp=datetime.datetime(2020, 1, 28, 12, 22)
		)


	@freeze_time("2020-01-28 12:33")
	@override_settings(
		TWILIO_ACCOUNT_SID='great-sid',
		TWILIO_AUTH_TOKEN='best-token',
		TWILIO_FROM='+13334445555',
		TWILIO_TO='+19099099099')
	@patch('ping.utils.Client')
	def test_only_one_ping_created_and_proper_sms_generated(self, Client):
		self.assertEqual(
			Ping.objects.filter(config=self.config_1).count(),
			0
		)
		management.call_command('check_pings')

		self.assertEqual(Ping.objects.all().count(), 1)
		ping, = Ping.objects.filter(config=self.config_1)

		self.assertEqual(
			ping.text, "How much water did you drink?"
		)

		Client.assert_called_once_with('great-sid', 'best-token')
		Client.return_value.messages.create.assert_called_once_with(
			to='+19099099099',
			from_='+13334445555',
			body='How much water did you drink?'
		)
