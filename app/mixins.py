import uuid
from django.db import models


class UidPrimaryModel(models.Model):
    """
    Объект с UUID первичным ключём
    """
    uid = models.UUIDField('UID', default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    class Meta:
        abstract = True


class StatusMixin(models.Model):
    """
    Модель с полем статуса
    """
    STATUS_NEW = 1
    STATUS_IN_PROGRESS = 2
    STATUS_DONE = 3

    STATUS_CHOICES = (
        (STATUS_NEW, "Новый"),
        (STATUS_IN_PROGRESS, "В работе"),
        (STATUS_DONE, "Сделано")
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=1, null=True)

    class Meta:
        abstract = True
