from django.db import models

class Place(models.Model):
    location = models.CharField(verbose_name="위치", max_length=128)
    pName = models.CharField(verbose_name="장소이름", max_length=200)
    purpose = models.CharField(verbose_name="장소 목적", max_length=128)
    sTime = models.DateField(verbose_name="활성화시작시간")
    eTime = models.DateField(verbose_name="활성화종료시간")
    basic_cate = models.CharField(verbose_name="기본카테고리", max_length=200)
    detail_cate = models.CharField(verbose_name="세부카테고리", max_length=200)
    require = models.CharField(verbose_name="필요조건", max_length=300, blank=True, null=True)
    link = models.URLField(verbose_name="링크", blank=True, null=True)
    thumbnail = models.ImageField(verbose_name="대표이미지", blank=True, null=True, upload_to='place_image')
    image1 = models.ImageField(verbose_name="이미지1", blank=True, null=True, upload_to='place_image')
    image2 = models.ImageField(verbose_name="이미지2", blank=True, null=True, upload_to='place_image')
    image3 = models.ImageField(verbose_name="이미지3", blank=True, null=True, upload_to='place_image')
    
    def __str__(self):
        return self.location
    