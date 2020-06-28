from django.contrib import admin
from .models import Runs, staffname, Permit, routes, front_trailer, back_trailer

admin.site.register(Runs)
admin.site.register(staffname)
admin.site.register(Permit)
admin.site.register(routes)
admin.site.register(front_trailer)
admin.site.register(back_trailer)
# Register your models here.
