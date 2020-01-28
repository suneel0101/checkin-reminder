from django.db import models


class PingConfig(models.Model):
	note = models.CharField(max_length=250, null=False, blank=False)
	ping_text = models.CharField(max_length=250, null=False, blank=False)
	minutes_interval = models.IntegerField(null=True, blank=True)
	active = models.BooleanField(default=True)
	start_timestamp = models.DateTimeField(null=False, blank=False)
	last_run_timestamp = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.note


class Ping(models.Model):
	config = models.ForeignKey(PingConfig, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	text = models.CharField(max_length=250, null=False, blank=False)
	response = models.CharField(max_length=250, null=True, blank=True)
	timestamp_responded = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.text