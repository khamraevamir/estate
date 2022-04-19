from django.contrib import admin
from . models import Flat, NewFlat, Home, Commercial, Land




class FlatAdmin(admin.ModelAdmin):
    list_display = ('title', 'rooms', 'square')

admin.site.register(Flat, FlatAdmin)


class NewFlatAdmin(admin.ModelAdmin):
    list_display = ('title', 'rooms', 'square')

admin.site.register(NewFlat, NewFlatAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'rooms', 'square')

admin.site.register(Home, HomeAdmin)



class CommercialAdmin(admin.ModelAdmin):
    list_display = ('title', 'rooms', 'square')

admin.site.register(Commercial, CommercialAdmin)


class LandAdmin(admin.ModelAdmin):
    list_display = ('title', 'square')

admin.site.register(Land, LandAdmin)