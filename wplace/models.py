#coding:utf-8
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Province(models.Model):
    province = models.CharField(max_length=20, db_index=True)

    def __unicode__(self):
        return self.province

    class Meta:
        verbose_name_plural = "省/自治区/直辖市"

class City(models.Model):
    city = models.CharField(max_length=30, db_index=True)
    
    def __unicode__(self):
        return self.city

    class Meta:
        verbose_name_plural = "市/自治州/区"

class Area(models.Model):
    area = models.CharField(max_length=30, db_index=True)

    def __unicode__(self):
        return self.area

    class Meta:
        verbose_name_plural = "县/自治县/街道"

class Address(models.Model):
    address = models.CharField(max_length=50, db_index=True, unique=True)

    def __unicode__(self):
        return self.address

    class Meta:
        verbose_name_plural = "地址"

class Position(models.Model):
    gps_position = models.CharField(max_length=47, db_index=True, unique=True)
    #mars_position = models.CharField(max_length=47) 

    def __unicode__(self):
        return self.gps_position

    class Meta:
        verbose_name_plural = "位置"

class Content(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name_plural = "内容"

NO_INTEGER_VALUE = 0
NO = 0
NO_VALUE = ""

class PlaceManager(models.Manager):

    def update_place(self, id, title, content, province, 
                     city, area, address, position):

        if position or title or address:
            place = Place.objects.get_place(id)
            place.title = title

            if province and province != place.province:
                place.province_id = Province.objects.get_or_create(province=province)[0].id
            if city and city != place.city:
                place.city_id = City.objects.get_or_create(city=city)[0].id

            if area and area != place.area:
                place.area_id = Area.objects.get_or_create(area=area)[0].id

            if address and address != place.address:
                place.address_id = Address.objects.get_or_create(address=address)[0].id

            if position and position != place.position:
                place.position_id = Position.objects.get_or_create(gps_position=position)[0].id
            if content and content != place.content:
                Content.objects.filter(id=place.content_id).update(content=content)

            place.save()
        else:
            place = False

        return place

    def get_place(self, place_id):
        if place_id.isdigit():
            try:
                place = Place.objects.get(id=place_id)
            except ObjectDoesNotExist:
                place = False
            if place:
                position_id = place.position_id
                address_id = place.address_id
                province_id = place.province_id
                city_id = place.city_id
                area_id = place.area_id
                content_id = place.content_id
                
                place.position = Position.objects.get(id=position_id) if position_id else NO_VALUE
                place.address = Address.objects.get(id=address_id) if address_id else NO_VALUE
                place.province = Province.objects.get(id=province_id) if province_id else NO_VALUE
                place.city = City.objects.get(id=city_id) if city_id else NO_VALUE
                place.area = Area.objects.get(id=area_id) if area_id else NO_VALUE
                place.content = Content.objects.get(id=content_id) if content_id else NO_VALUE
        else:
            place = False
                
        return place

    def add_place(self, title, position, province, 
                  city, area, address, content):

        if position or title or address:

            if position:
                position_id = Position.objects.get_or_create(gps_position=position)[0].id
            else:
                position_id = NO

            if province:
                province_id = Province.objects.get_or_create(province=province)[0].id
            else:
                province_id = NO

            if city:
                city_id = City.objects.get_or_create(city=city)[0].id
            else:
                city_id = NO

            if area:
                area_id = Area.objects.get_or_create(area=area)[0].id
            else:
                area_id = NO

            if address:
                address_id = Address.objects.get_or_create(address=address)[0].id
            else:
                address_id = NO

            if content:
                content_id = Content.objects.create(content=content).id
            else:
                content_id = NO

            wplace = Place.objects.create(title=title, position_id=position_id,
                    province_id=province_id, city_id=city_id, area_id=area_id,
                    address_id=address_id, content_id=content_id)
        else:
            wplace = False

        return wplace


class Place(models.Model):
    title = models.CharField(max_length=20)
    #owner = models.ForeignKey(Account)
    position_id = models.IntegerField(default=NO, db_index=True)
    province_id = models.IntegerField(default=NO, db_index=True)
    city_id = models.IntegerField(default=NO, db_index=True)
    area_id = models.IntegerField(default=NO, db_index=True)
    address_id = models.IntegerField(default=NO, db_index=True)
    content_id = models.IntegerField(default=NO)
    objects = PlaceManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "地点"

class ContentPicture(models.Model):
    content_id = models.IntegerField()
    sequence_no = models.IntegerField()
    picture_no = models.IntegerField()
    strorage_path = models.CharField(max_length=10, default='')

    class Meta: verbose_name_plural = "图片"
    
