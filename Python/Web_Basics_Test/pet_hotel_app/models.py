from django.db import models


class PetOwner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_owner'


class Cat(models.Model):
    owner = models.ForeignKey('PetOwner', models.CASCADE)
    name = models.CharField(max_length=15)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat'


class CatRoom(models.Model):
    cat = models.ForeignKey(Cat, models.CASCADE)
    hotel = models.ForeignKey('Hotel', models.CASCADE)
    register_date = models.DateField()
    unregister_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'cat_room'


class Dog(models.Model):
    owner = models.ForeignKey('PetOwner', models.CASCADE)
    name = models.CharField(max_length=15)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dog'


class DogRoom(models.Model):
    dog = models.ForeignKey(Dog, models.CASCADE)
    hotel = models.ForeignKey('Hotel', models.CASCADE)
    register_date = models.DateField()
    unregister_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'dog_room'


class Hotel(models.Model):
    name = models.CharField(max_length=25)
    stars = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hotel'

# Create your models here.
