from django.core.management.base import BaseCommand
from app.excel import ExcelUtils
from app.utils import get_excel_rows_not_generated_url, create_url_from_rows


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        row_qs = get_excel_rows_not_generated_url()
        create_url_from_rows(row_qs)
