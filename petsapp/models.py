from django.db import models

# Create your models here.
class HomeDB(models.Model):
    home_image = models.ImageField(upload_to='images', null=True)
    home_heading = models.CharField(max_length=1000)
    home_content = models.CharField(max_length=2000)

    
class animalsDB(models.Model):
    animals_image = models.ImageField(upload_to='images', null=True)
    animals_heading = models.CharField(max_length=1000)
    animals_content = models.CharField(max_length=2000)
    animals_price = models.IntegerField(max_length=6)
    animals_isStock = models.BooleanField(default=False)
