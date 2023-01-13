import re
import random
from typing import List
from django.db import models
from psycopg2 import IntegrityError
from django.conf import settings
from jsonfield import JSONField
from shortener.mixins import UidPrimaryModel


class Template(UidPrimaryModel):
    title = models.CharField(max_length=255, blank=False)
    template_url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str('Шаблон - ' + self.title)

    def get_field_names(self) -> List[str]:
        """
        Получение списка строк подстановки
        """
        fields = re.findall(r'{([^}]+)}', self.template_url)
        return fields


class URL(UidPrimaryModel):
    created_at = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=15, unique=True, blank=True)
    long_url = models.URLField()

    # template_fields = JSONField(verbose_name='Значение строк подстановки')

    template = models.ForeignKey(Template, models.PROTECT, null=True, blank=True)

    is_qr_generated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.long_url} to {self.code}'

    def _generate_code(self):
        self.code = ''.join(random.choice(settings.SHORT_URL_ALPHABET) for _ in range(settings.SHORT_URL_SIZE))

    def get_short_url(self):
        return settings.SHORT_URL_PREFIX + self.code

    def save(self, *args, **kwargs):
        while True:
            try:
                # если кода нет, то генерируем
                if not self.code:
                    # self._generate_date_death()
                    self._generate_code()
                super().save(*args, **kwargs)
                break
            except IntegrityError as e:
                try:
                    link = self.objects.get(url=self.long_url)
                    self.__dict__.update(link.__dict__)
                except URL.DoesNotExist:
                    continue

    def set_is_generated(self):
        self.is_qr_generated = True


class ExcelRow(UidPrimaryModel):
    template_passes = JSONField()
    template = models.ForeignKey(Template, models.PROTECT, null=True, blank=True)
    is_url_generated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.uid)

    def set_is_url_generated(self):
        self.is_url_generated = True


class File(UidPrimaryModel):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, null=True)
    excel = models.FileField(upload_to="documents/excel")
    is_parsed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.uid)

    def set_parsed(self):
        self.is_parsed = True
