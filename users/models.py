from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  fullname = models.CharField(max_length=225)
  username = models.CharField(max_length=225)
  email = models.EmailField(max_length=254, unique=True)
  phone = models.CharField(max_length=14)
  address = models.CharField(max_length=243)
  profile_pix = models.ImageField(upload_to='profile_pix',default='img/userav.png')


  

  def __str__(self):
   return self.fullname
 