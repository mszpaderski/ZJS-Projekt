from django.db import models
from django.conf import settings
# Create your models here.

class Character_sheet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length = 40)
    GENDER_CHOICES = (
        ('M', 'Mężczyzna'),
        ('F', 'Kobieta'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    RACE_CHOICES = (
        ('H', 'Człowiek'),
        ('O', 'Ork'),
        ('E', 'Elf'),
        ('D', 'Krasnolud'),
    )
    race = models.CharField(max_length=1, choices=RACE_CHOICES, default='H')
    CLASS_CHOICES = (
        ('W', 'Wojownik'),
        ('R', 'Łotrzyk'),
        ('M', 'Mag'),
        ('C', 'Kusznik'),
    )
    class_x = models.CharField(max_length=1, choices=CLASS_CHOICES, default='W')
    gold = models.IntegerField(default = 1000)
    
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    
class Equipment(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField(default = 0)
    WEAPON_TYPE_CHOICES = (
        ('M', 'Broń ręczna'),
        ('D', 'Broń zasięgowa'),
        ('A', 'Pancerz/Ubiór'),
        ('C', 'Użytkowy'),
    )
    weapon_type = models.CharField(max_length=1, choices=WEAPON_TYPE_CHOICES, default='C')
    description = models.TextField(max_length = 300)
    owned_by = models.ManyToManyField(Character_sheet)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name