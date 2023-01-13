from django.core.management.base import BaseCommand
from shortener.models import URL, ExcelRow, File


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        URL.objects.all().delete()
        ExcelRow.objects.all().delete()
        File.objects.all().delete()
