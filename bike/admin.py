from django.contrib import admin
from bike.models import Person,Passenger,Driver,Notification


admin.site.register(Person)
admin.site.register(Passenger)
admin.site.register(Driver)
admin.site.register(Notification)
# Register your models here.
