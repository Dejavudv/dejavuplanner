from django.contrib import admin
from userauths.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'bio', "phone"]

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject']

class JobOfferAdmin(admin.ModelAdmin):
    list_display = ['about', 'email']

admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(JobOffer,JobOfferAdmin)

