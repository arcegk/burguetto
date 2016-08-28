from __future__ import unicode_literals

from django.db import models

from .choices import SECTION

class Ingredient(models.Model):
	image_path = models.TextField()
	name = models.CharField(max_length=30)
	extra_price = models.FloatField()
	section = models.CharField(choices=SECTION, max_length=30)
