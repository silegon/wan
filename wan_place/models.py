from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=50)

class wanPosition(models.Model):
    gps_position = models.CharField(max_length=47)
    #mars_position = models.CharField(max_length=47) 
    address = models.IntegerField(Address)

class wanPlace(models.Model):
    title = models.CharField(max_length=20)
    position = models.IntegerField(wanPosition)
    #owner = models.ForeignKey(Account)
    content_id = models.IntegerField()

class ContentPicture(models.Model):
    content_id = models.IntegerField()
    sequence_no = models.IntegerField()
    picture_no = models.IntegerField()

class Content(models.Model):
    content = models.TextField()
    
