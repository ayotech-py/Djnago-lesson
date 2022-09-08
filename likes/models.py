from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class LikedItem(models.Model):
    likes = models.ForeignKey(User, on_delete=models.CASCADE)
    #contenttype for identiying the type of object that the user likes
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #object id for referencing the particular object
    object_id = models.PositiveIntegerField()
    #For reading the actual object
    content_object = GenericForeignKey()