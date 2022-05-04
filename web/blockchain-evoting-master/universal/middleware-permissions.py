from django.contrib.auth.models import Group 
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.urls import reverse

class GetUserInGroup:

    def __init__(self, get_response):  
        self.get_response = get_response
        self.usergroup = ""

    def __call__(self, request): 
        
        reinsurance = None
        retail = None
        try:
            reinsurance =  Group.objects.get(name='reinsurance') 
            retail =  Group.objects.get(name='retail') 
        except:
            pass

        # try:
        
        if(request.path.find("/home/") > -1 or request.path.find("/admin/") > -1 ):
            
            pass
        elif(reinsurance in request.user.groups.all() and retail not in request.user.groups.all() ):
            self.usergroup = "reinsurance"
            pass
        
        elif(reinsurance not in request.user.groups.all() and retail in request.user.groups.all() ):
            self.usergroup = "retail"
            pass
        else:
            raise PermissionDenied   

  
        # except:
        #     raise PermissionDenied
      
        request.my_group = self.usergroup
        response = self.get_response(request) 
        return response  

 
 