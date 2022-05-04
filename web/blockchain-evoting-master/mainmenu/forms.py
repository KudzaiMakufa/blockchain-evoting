from django import forms
from mainmenu.models import MainMenu

class MenuForm(forms.Form):

  

    name = forms.CharField(widget= forms.TextInput(
        attrs={
         
            "type" : "text",
            "class":"form-control"
        }
    ))

    url = forms.CharField(widget= forms.TextInput(
        attrs={
         
            "type" : "text",
            "class":"form-control"
        }
    ))

    permissions = forms.CharField(widget= forms.TextInput(
        attrs={
         
            "type" : "text",
            "class":"form-control"
        }
    ))

    icon_class = forms.CharField(widget= forms.TextInput(
        attrs={
         
            "type" : "text",
            "class":"form-control"
        }
    ))

    has_submenu = forms.CharField(widget= forms.TextInput(
        attrs={
         
            "type" : "text",
            "class":"form-control"
        }
    ))


class SubMenuForm(forms.Form):

  

    name = forms.CharField(widget= forms.TextInput(
        attrs={
         
            "type" : "text",
            "class":"form-control"
        }
    ))

    mainmenu = forms.ModelChoiceField(required=True, widget=forms.Select(attrs={ "class":"form-control custom-select"}), queryset=MainMenu.objects.filter())
    url = forms.CharField(  widget= forms.TextInput(
        attrs={
         
            "type" : "text",
            "class":"form-control"
        }
    ))

    permissions = forms.CharField(widget= forms.TextInput(
        attrs={
            "type" : "text",
            "class":"form-control"
        }
    ))

    icon_class = forms.CharField(widget= forms.TextInput(
        attrs={
         
            "type" : "text",
            "class":"form-control"
        }
    ))

   
 