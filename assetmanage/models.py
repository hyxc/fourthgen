from django.db import models

# Create your models here.
class Assetmanage(models.Model):
    asset_num =  models.CharField(max_length = 50)
    device_type = models.CharField(max_length = 50)
#    brand = models.CharField(max_length = 10)
#    type = models.CharField(max_length = 20)
    local_ip = models.CharField(max_length = 20)
    remote_ip = models.CharField(max_length = 20)
    system_type = models.CharField(max_length = 20)
#    disksize = models.CharField(max_length = 10)
#    disknum = models.CharField(max_length = 10)
#    diskraid = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.asset_num
