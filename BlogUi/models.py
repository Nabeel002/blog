from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime

# Create your models here.


class Article(models.Model):
    Author=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="Choose the author")
    title=models.CharField(max_length=255)
    date=models.DateField(default=datetime.date.today)
    body=RichTextField(blank=True,null=True)   
    tags=['tech','bussiness','current affair','news','politics']
    preview_image=models.ImageField(upload_to='uploads/',null=True,blank=True)
    preview_text=models.TextField(max_length=100,blank=True,null=True)
    
    
    def __str__(self):
        return self.title 

    
class Comment(models.Model):
    post=models.ForeignKey(Article,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(default=datetime.date.today)
    name=models.CharField(max_length=100,blank=True,null=True)
    comment=models.TextField(max_length=300,null=True,blank=True)






    



class contact(models.Model):
    email=models.EmailField(max_length=250,blank=True)
    req=models.CharField(max_length=500,null=True,blank=True,verbose_name="Please Submit The Request here")
    

    class Meta:
        verbose_name = "Email"

    def __str__(self):
        return self.email



class Prompt(models.Model):
    section=models.CharField(null=True,blank=True,max_length=250)
    title=models.TextField(null=True,blank=True,max_length=250)
    topics=models.TextField(null=True,blank=True,max_length=250)




