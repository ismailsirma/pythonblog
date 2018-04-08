from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120) # character field.
    content = models.TextField() 
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

 # auto_now : whenever is is changed, it will be set.
 # auto_now_add : record added one time.

    def __unicode__(self): #in ptyhon 2
        return self.title

    def __str__(self):
        return self.title