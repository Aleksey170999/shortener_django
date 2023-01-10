import uuid
from django.db import models


class UidPrimaryModel(models.Model):
    """
    Объект с UUID первичным ключём
    """
    uid = models.UUIDField('UID', default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    class Meta:
        abstract = True
