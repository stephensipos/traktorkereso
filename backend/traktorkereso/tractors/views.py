#from django.shortcuts import render
from http import HTTPStatus
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Tractor
from .models import Equipment

# Create your views here.

class TractorView(View):
    def get(self, request, tractor_id):
        try:
            tractor = Tractor.objects.get(pk=tractor_id)
            equipments = Equipment.objects.filter(tractor__id=tractor_id)

            equipment_arr = [e.name for e in equipments]

            return JsonResponse({
                "make": tractor.make,
                "model": tractor.model,
                "price": tractor.price,
                "year": tractor.year,
                "condition": tractor.condition.description,
                "hours": tractor.hours,
                "engine_power": tractor.engine_power,
                "documents_valid": tractor.documents_valid,
                "documents_type": tractor.documents_type,
                "description": tractor.documents_valid,
                "image_url": tractor.image_url,
                "fuel_type": tractor.fuel_type,
                "equipment": equipment_arr
            })

        except:
            return JsonResponse(
                {"error_code": 1},
                status=HTTPStatus.NOT_FOUND
            )            


class Rating(View):
    def get(self, request, tractor, user):
        try:


            return JsonResponse({
                "tractor_id": rating.tractor,
                "username": rating.user,
                "stars": rating.stars,
                "comment": rating.comment,
            })

        except:
            return JsonResponse(
                {"error_code": 1},
                status=HTTPStatus.NOT_FOUND
            )