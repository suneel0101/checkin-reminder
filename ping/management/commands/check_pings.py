from django.core.management.base import BaseCommand
from ping.models import PingConfig
from ping.utils import create_ping_and_send_sms


class Command(BaseCommand):

    def handle(self, *args, **options):
        configs = PingConfig.objects.filter(active=True)
        for config in configs:
            if config.needs_to_be_run:
                create_ping_and_send_sms(config)
