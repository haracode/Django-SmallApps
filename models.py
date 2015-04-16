from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class JoinNow(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True) #null is for db, blank for forms
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField() #() defaults to null=False
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #auto_now_add when created make timestamp
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #auto_now updated timestamp
    
    def __unicode__(self):
        return smart_unicode(("%s %s %s") %(self.first_name, self.last_name, self.email))#use smart unicode for emails or characters with accents
    