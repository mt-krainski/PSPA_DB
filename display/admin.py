from django.contrib import admin

from .models import *

admin.site.register(Member)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(AreaOfExpertise)
admin.site.register(Company)
admin.site.register(JobDescription)