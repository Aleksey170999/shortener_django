from django.core.management.base import BaseCommand
from shortener.excel import ExcelUtils


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        excel_utils = ExcelUtils()
        row_qs = excel_utils.get_excel_rows_not_generated_url()
        excel_utils.create_url_from_rows(row_qs)
