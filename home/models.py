from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(blank=True)    
    data = models.DateField(blank=True,null=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"