import json
from http import HTTPStatus

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.authtoken.models import Token

# Create your views here.


class Login(View):
    def post(self, request):
        body = json.loads(request.body)
        username = body.get("username")
        password = body.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            return JsonResponse(
                {"error_code": 1},
                status=HTTPStatus.UNAUTHORIZED
            )
        else:
            try:
                token = Token.objects.create(user=user)
            except IntegrityError:
                token = Token.objects.get(user=user)

            return JsonResponse(
                {"bearer": token.key}
            )
        

class Register(View):
    def post(self, request):
        body = json.loads(request.body)

        # Check if username exists
        username=body.get("username", "").strip()
        
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
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)

            return JsonResponse({
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            })

        except:
            return JsonResponse(
                {"error_code": 1},
                status=HTTPStatus.NOT_FOUND
            )

