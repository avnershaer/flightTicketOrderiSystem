from django.shortcuts import render, HttpResponse
from .forms import UserRoleForm




def index(request):
    return HttpResponse('OK!!!!!!!!!!!')


def userRole(request):
    form = UserRoleForm(request.GET)
    return render(request=request, template_name='flghts_order_system/userRoleForm.html', context={'form':form})
