from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import MenuForm , SubMenuForm
from .models import MainMenu,SubMenu
from django.contrib import messages

@login_required
def menu_list(request):
    menus  = MainMenu.objects.all()
    context = {
        'menus':menus
    }
    return render(request , "mainmenu/menu_list.html" , context) 


@login_required
def menu_create(request):
    form = None
    
    print(request.method)
    if request.method == 'POST':
        form = MenuForm(request.POST)
    
        if form.is_valid():
            data = form.cleaned_data
            mainmenu = MainMenu(**data)
            mainmenu.save()
            messages.add_message(request, messages.INFO, ' Menu created')
            return HttpResponseRedirect('/mainmenu/menu_create')
            

    else:
        form = MenuForm()
    context = {
        'form':form
    }
    

    return render(request , "mainmenu/menu_create.html" , context) 
@login_required
def link_list(request):
    links  = SubMenu.objects.all()
    context = {
        'links':links
    }

    return render(request , "mainmenu/link_list.html" , context) 
@login_required
def link_create(request):
    form = None
    
    print(request.method)
    if request.method == 'POST':
        form = SubMenuForm(request.POST)
    
        if form.is_valid():
            data = form.cleaned_data
            submenu = SubMenu(**data)
            submenu.save()
            messages.add_message(request, messages.INFO, ' Submenu created')
            return HttpResponseRedirect('/mainmenu/link_create')
            

    else:
        form = SubMenuForm()
    # print(form)
    context = {
        'form':form
    }
    

    return render(request , "mainmenu/link_create.html" , context) 