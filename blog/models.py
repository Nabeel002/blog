from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Post(models.Model):
    preview_field=models.TextField(max_length=100,blank=True,null=True)
    author=models.ForeignKey('auth.user',on_delete=models.DO_NOTHING)
    post_image=models.ImageField(blank=False,upload_to="images/")
    title=models.CharField(max_length=150)
    text=RichTextUploadingField(blank=True,null=True)
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    @property
    def image_url(self):
     if self.post_image and hasattr(self.post_image, 'url'):
        return self.post_image.url
      
         
            


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    


    def __str__(self):
        return self.title



class Comment(models.Model):
    post=models.ForeignKey('blog.post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)


    def approve(self):
        self.approved_comment=True
        self.save()


    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
    

    def __str__(self):
        self.text