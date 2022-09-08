from tkinter import CASCADE
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tags(models.Model):
    label = models.CharField(max_length=225)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    
    #To define a generic relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    #Getting the actual object/product that this tag is applied to when querying data
    content_object = GenericForeignKey()