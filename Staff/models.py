from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Staff(models.Model):
	Male = 'Male'
	Female = 'Female'
	SEX_CHOICES = ((Male,'Male'),(Female,'Female'))
	first_name = models.CharField(max_length = 40)
	last_name = models.CharField(max_length = 40)
	age = models.IntegerField(max_length = 3)
	sex = models.CharField(max_length=7,choices = SEX_CHOICES, default=Male)
	salary = models.FloatField(max_length = 15)
	position = models.CharField(max_length = 40)
	def __str__(self):
		return self.first_name+' '+self.last_name
