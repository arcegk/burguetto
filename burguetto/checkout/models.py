from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

class Checkout(models.Model):
	address = models.CharField(max_length=40)
	selections = JSONField()

	
