from django.contrib import admin
from .models import *
# Register your models here.

class MasterAdmin(admin.ModelAdmin):
    pass

admin.site.register(MilitaryChief, MasterAdmin)
admin.site.register(PoliticalLeader, MasterAdmin)
admin.site.register(ArmedGroup, MasterAdmin)
admin.site.register(Division, MasterAdmin)
admin.site.register(Organization, MasterAdmin)
admin.site.register(Conflict, MasterAdmin)
admin.site.register(Weapon, MasterAdmin)
admin.site.register(Dealer, MasterAdmin)
admin.site.register(SupplyWeaponArmedGroupDealer, MasterAdmin)
admin.site.register(DialogPoliticalLeaderArmedGroupOrganization, MasterAdmin)
admin.site.register(EnterPart, MasterAdmin)
admin.site.register(ExitPart, MasterAdmin)
admin.site.register(EnterMed, MasterAdmin)
admin.site.register(ExitMed, MasterAdmin)
admin.site.register(CanSupply, MasterAdmin)
admin.site.register(Religious, MasterAdmin)
admin.site.register(Economic, MasterAdmin)
admin.site.register(Region, MasterAdmin)
admin.site.register(Etnic, MasterAdmin)
admin.site.register(PoliticalLeadersMilitaryChiefs, MasterAdmin)