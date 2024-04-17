from django.contrib import admin
from .models import Member, Media, Event, Activities, PhotoGallary, Slider

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'nid_no', 'mobile_no')

admin.site.register(Member, MemberAdmin)

admin.site.register(Media)
admin.site.register(Event)
admin.site.register(Activities)
admin.site.register(Slider)
admin.site.register(PhotoGallary)