from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Link(models.Model):
    #author = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name = "Yazar")
    vid_link = models.CharField(max_length=50,verbose_name="Youtube Link : ")
    def __str__(self):
        return self.title


class Document(models.Model):
    document = models.FileField(blank=True,null=True)