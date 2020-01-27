from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Address

#admin.site.register(User, UserAdmin)

admin.site.register(Address)

@admin.register(User)
class MyModelAdmin(admin.ModelAdmin):

    fields = ('email','username','last_name','first_name')



