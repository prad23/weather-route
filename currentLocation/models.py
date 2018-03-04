from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Network(models.Model):
    device_text = models.CharField(max_length=15)
    macaddress_text = models.CharField(max_length=50)
    pub_date = models.DateField('date published')

class CNetwork(models.Model):
    device = models.ForeignKey(Network,on_delete=models.CASCADE)
