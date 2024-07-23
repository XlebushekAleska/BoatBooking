from django.contrib import admin
# from .models import Boats, Bookings, Tariffs, Notifications
from .models import Boat, Booking, Tariff, Notification

# admin.site.register(Boats)
# admin.site.register(Bookings)
# admin.site.register(Tariffs)
# admin.site.register(Notifications)

admin.site.register(Boat)
admin.site.register(Booking)
admin.site.register(Tariff)
admin.site.register(Notification)
