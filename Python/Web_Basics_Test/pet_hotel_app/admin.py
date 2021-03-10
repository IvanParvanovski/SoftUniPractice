from django.contrib import admin

from pet_hotel_app.models import PetOwner, Cat, CatRoom, Dog, DogRoom, Hotel

admin.site.register(PetOwner)
admin.site.register(Cat)
admin.site.register(CatRoom)
admin.site.register(Dog)
admin.site.register(DogRoom)
admin.site.register(Hotel)

# Register your models here.
