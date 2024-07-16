from django.contrib import admin
from .models import User, Template, Hosting, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Template)
admin.site.register(Hosting)
admin.site.register(Order)