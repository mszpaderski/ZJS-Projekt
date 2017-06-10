from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import loader
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group

from .models import Character_sheet, Equipment
from .forms import Character_sheet_form, Equipment_form
# Create your views here.


#CHARACTERS
#LIST
def characters_list(request):
    querydata = Character_sheet.objects.all()
    passed_data = {
        "querydata": querydata,
        "title": "Lista Postaci"
    }
    return render(request, "characters/list.html", passed_data)

#DETAIL
def characters_detail(request, id):
    instance = get_object_or_404(Character_sheet, id=id)
    equipment = instance.equipment_set.all()
    passed_data = {
        "instance": instance,
        "title": instance.name,
        "equipment": equipment
    }
    return render(request, "characters/detail.html", passed_data)

#CREATE
def characters_new(request):
    
    if request.user.groups.filter(name="Player").exists():
    
        form = Character_sheet_form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect(characters_list)
        passed_data = {
            "form": form,
            "title": "Nowa Postać"
        }
        return render(request, "characters/new.html", passed_data)
    else:
        raise Http404


#EQUIPMENT
#LIST
def equipment_list(request):
    querydata = Equipment.objects.all()
    passed_data = {
        "querydata": querydata,
        "title": "Lista Ekwipunku"
    }
    return render(request, "equipment/list.html", passed_data)

#DETAIL
def equipment_detail(request, id):
    instance = get_object_or_404(Equipment, id=id)
    characters = get_list_or_404(Character_sheet, user=request.user)
    if request.method == "POST":
        character_id = request.POST.get("character_name")
        character_buy = get_object_or_404(Character_sheet, id=character_id)
        if character_buy.gold >= instance.price: #if afford
            current_gold = character_buy.gold - instance.price
            instance.owned_by.add(character_buy)
            instance.save()
            Character_sheet.objects.filter(id=character_buy.id).update(gold=current_gold)
            messages.success(request, "Kupiono!")
        else:
            messages.error(request, "Za mało pieniędzy!")
            
    passed_data = {
        "instance": instance,
        "title": instance.name,
        "characters": characters
    }
    return render(request, "equipment/detail.html", passed_data)

#CREATE
def equipment_new(request):
    if request.user.groups.filter(name="Game Master").exists():
        form = Equipment_form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(equipment_list)
        passed_data = {
            "form": form,
            "title": "Nowy Ekwipunek"
        }
        return render(request, "equipment/new.html", passed_data)
    else:
        raise Http404