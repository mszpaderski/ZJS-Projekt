from django.contrib import admin

# Register your models here.

from character_sheet.models import Character_sheet, Equipment

class Character_admin(admin.ModelAdmin):
    list_display = ["__unicode__","gender","race","class_x","gold"]
    class Meta:
        model = Character_sheet
        
        
class Equipment_admin(admin.ModelAdmin):
    list_display = ["__unicode__","price","weapon_type","description"]
    class Meta:
        model = Equipment

admin.site.register(Character_sheet, Character_admin)

admin.site.register(Equipment, Equipment_admin)