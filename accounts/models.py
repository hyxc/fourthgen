from django.db import models
import hashlib
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def save(self,*args,**kwargs):
        self.password = hashlib.sha1(self.password+self.username+'ylhb').hexdigest()
        super(User,self).save(*args,**kwargs)

    def __unicode__(self):
        return self.username

