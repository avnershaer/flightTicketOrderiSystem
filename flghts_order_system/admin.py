from django.contrib import admin

from .models import *

admin.site.register(UserRole)
admin.site.register(Users)
admin.site.register(Adminstrators)
admin.site.register(Customers)
admin.site.register(AirLineCompanies)
admin.site.register(Countries)
admin.site.register(Flights)
admin.site.register(Tickets)

