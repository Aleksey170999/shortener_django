from django.core.management.base import BaseCommand
from shortener.excel import ExcelUtils


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        excel_utils = ExcelUtils()
        excel_utils.parse_not_parsed_files()
