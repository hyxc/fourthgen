from django.db import models

# Create your models here.
class Assetmanage(models.Model):
    asset_num =  models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    server_ip = models.CharField(max_length = 20)
    remote_ip = models.CharField(max_length = 20)
    data_center = models.CharField(max_length = 50)
    room_num = models.CharField(max_length = 20)
    rack_num = models.CharField(max_length = 20)
    system_type = models.CharField(max_length = 20,default='-')
    cputype_num = models.CharField(max_length = 20,default='-')
    disksize_num = models.CharField(max_length = 20,default='-')
    memsize_num = models.CharField(max_length = 20,default='-')
    disk_raid = models.CharField(max_length = 20,default='-')
    card_type_num = models.CharField(max_length = 20,default='-')
    power_num = models.CharField(max_length = 20,default='-')
    service_num = models.CharField(max_length = 50)
    buy_time = models.CharField(max_length = 50,default='-')
    expiration_time = models.CharField(max_length = 50,default='-')
    note = models.CharField(max_length = 200,default='-')

    def __unicode__(self):
        return self.asset_num

class Hostinfo(models.Model):
    host_ip =  models.ForeignKey(Assetmanage,related_name='asset_set')
    local_ip = models.CharField(max_length = 20)
    app = models.CharField(max_length = 50,default='-')
    host_name = models.CharField(max_length = 20)
    system_version = models.CharField(max_length = 20)
    cpu_num =  models.CharField(max_length = 20)
    disk_size = models.CharField(max_length = 20)
    mem_size = models.CharField(max_length = 20)
    host_note = models.CharField(max_length = 200,default='-')

    def __unicode__(self):
        return self.local_ip

