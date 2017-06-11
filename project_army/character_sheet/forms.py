from django import forms

from .models import Character_sheet, Equipment

class Character_sheet_form(forms.ModelForm):
    class Meta:
        model = Character_sheet
        fields = [
            "name",
            "gender",
            "race",
            "class_x"
        ]
        
class Equipment_form(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            "name",
            "price",
            "weapon_type",
            "description"
        ]