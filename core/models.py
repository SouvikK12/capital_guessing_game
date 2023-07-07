from django.db import models
import uuid


class Country_and_Capital(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    country = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)