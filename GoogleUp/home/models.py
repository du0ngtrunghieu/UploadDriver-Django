from django.db import models
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()
# Create your models here.
class Map(models.Model):
    
    id = models.AutoField( primary_key=True)
    map_name = models.CharField(max_length=200)
    map_data = models.ImageField(upload_to='maps/', storage=gd_storage)
    video = models.FileField(upload_to='videos/',storage=gd_storage,null=True)