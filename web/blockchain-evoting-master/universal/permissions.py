# from django.contrib.auth.models import Group 
# from django.http import HttpResponseForbidden
# from django.http import HttpResponse
# from django.core.exceptions import PermissionDenied
# from django.urls import reverse


# def useringroup(self , user):
#     self.user = user
#     reinsurance =  Group.objects.get(name='reinsurance') 
#     retail =  Group.objects.get(name='retail') 
#     if(reinsurance in user.groups.all() and retail not in user.groups.all() ):
#         pass

#     elif(reinsurance not in user.groups.all() and retail in user.groups.all() ):
#         pass
#     elif user.is_superuser:
#         pass
#     else:
#         raise PermissionDenied

from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='/dashboard')