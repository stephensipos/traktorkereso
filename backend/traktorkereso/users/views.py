import json
from http import HTTPStatus

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth.models import User

# Create your views here.


class Login(View):
    def post(self, request):
        return JsonResponse({})

class Register(View):
    def post(self, request):
        body = json.loads(request.body)

        # Check if username exists
        username=body.get("username", "").strip().lower()

        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"error_code": 1},
                status=HTTPStatus.CONFLICT
            )

        # Check if email exists
        email=body.get("email", "").strip().lower()

        if User.objects.filter(email=email).exists():
            return JsonResponse(
                {"error_code": 2},
                status=HTTPStatus.CONFLICT
            )
        
        # Create user
        password=body.get("password")
        first_name=body.get("first_name", "")
        last_name=body.get("last_name", "")

        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        return HttpResponse(status=HTTPStatus.CREATED)
    

class Users(View):
    def get(self, request):
        return JsonResponse({})