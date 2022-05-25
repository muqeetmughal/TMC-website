from django.contrib import admin
from .models import Contact, Gallery, JobApplication, Newsletter, Page, Settings, Clients, Slider, Team, User
# Register your models here.


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


admin.site.register(User)
admin.site.register(Gallery)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Newsletter)
admin.site.register(Contact)
admin.site.register(Clients)
admin.site.register(Slider)
admin.site.register(Page)
admin.site.register(Team)
admin.site.register(JobApplication)
# admin.site.register(MenuPage)
# admin.site.register(Menu)
