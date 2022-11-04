from django.db import models

class My(models.Model):

   
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=100)
   

    class Meta :
        ordering=['id']