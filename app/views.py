import profile
from django.shortcuts import render
from .models import User,Customer
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view

@api_view(('GET','POST'))
def register_page(request):
    if request.method == "POST":
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        mobile=request.data['mobile']
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email,mobileno=mobile)
        cust=Customer.objects.create(
            user=user,
            profile_no=user.id
        )
        return Response({"message":"Registration done"})
    return Response({"first_name":"","last_name":"","email":"","mobile":""})
