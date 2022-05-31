from django.contrib import admin
from DjangoWeb.models import Profile, Content, RentCar, BorrowCar
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_created')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'subject', 'message', 'message_created_time')

class RentCarAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email', 'pickup_location', 'dropoff_location', 'pickup_date', 'dropoff_date', 'pickup_time', 'remarks', 'rent_number', 'order_date_created')

class BorrowCarAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'Car_Id', 'Car_Name', 'Car_Description', 'Car_Rental_Price', 'CarImage', 'Car_borrow_created')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(RentCar, RentCarAdmin)
admin.site.register(BorrowCar, BorrowCarAdmin)