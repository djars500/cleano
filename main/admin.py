from django.contrib import admin
from .models import Courier,Zayavka, Contact, Usluga,Place, Result


class ZayavkaAdmin(admin.ModelAdmin):
    list_filter = ('courier', )

admin.site.register(Courier)
admin.site.register(Zayavka, ZayavkaAdmin)
admin.site.register(Contact)
admin.site.register(Usluga)
admin.site.register(Place)
admin.site.register(Result)
