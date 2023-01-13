from django.core.management.base import BaseCommand
from shortener.qr_generator import QRGenerator


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        qr_gen = QRGenerator()
        qs = qr_gen.get_urls_no_qr()
        qr_gen.generate_all(qs)
