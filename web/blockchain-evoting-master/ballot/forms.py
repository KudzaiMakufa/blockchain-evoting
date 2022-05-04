from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from ballot.models import Candidate


class CandidateForm(forms.ModelForm):

    class Meta:

        model = Candidate
        
        

        fields = ['name','surname','national_id','address', 'photo']

        widgets  = {

            'name': forms.TextInput(attrs={
                "class":"form-control",
             
            }),

            'surname': forms.TextInput(attrs={
                "class":"form-control",
             
            }),
          
            'national_id': forms.TextInput(attrs={
                "class":"form-control",
              
            }),

            'address': forms.TextInput(attrs={
                "class":"form-control",
             
            }),
            'photo': forms.ClearableFileInput(
                attrs={
                
                    "type" : "file",
                    "class":"form-control"
                }
            ),
      
            
            
          

            


        }

