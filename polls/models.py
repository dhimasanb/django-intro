from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dhimas(models.Model):
    dhimas_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

class Ganteng(models.Model):
    dhimas = models.ForeignKey(Dhimas, on_delete=models.CASCADE)
    ganteng_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
