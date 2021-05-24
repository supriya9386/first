from django.db import models
from django.db import Q

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=30,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=25,unique=True)
    url=models.URLField(max_length=40)

    def __str__(self):
        return self.name


class Acess_records(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    webpages=webpages.objects.filter(Q(condition1)& Q(condition2)....)

    

    