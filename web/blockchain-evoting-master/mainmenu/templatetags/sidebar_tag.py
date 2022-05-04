from django import template
from django.contrib.auth.models import Group 
from mainmenu.models import MainMenu
from mainmenu.models import SubMenu

register = template.Library() 
from django.contrib.auth.models import User

@register.simple_tag
def get_username_from_userid(user_id):
    try:
        return User.objects.get(id=user_id).username
    except User.DoesNotExist:
        return 'Unknown'

@register.filter
def add_space(value):
    return value.replace("_"," ")

@register.filter(name='getallmenus') 
# def has_group(user, group_name):
#     group = Group.objects.filter(name=group_name)
#     if group:
#         group = group.first()
#         return group in user.groups.all()
#     else:
#         return False
def getallmenus(userid,name) :
    
   menus = MainMenu.objects.all()
    

   return menus



@register.filter(name='getsubmenu') 
def getsubmenu(menu_id,name) :
    
   submenus = SubMenu.objects.filter(mainmenu=menu_id)
    

   return submenus





