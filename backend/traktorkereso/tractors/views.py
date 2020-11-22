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


class TractorList(View):
    def get(self, request):
        try:
            filter_params = {}
            for key, val in request.GET.items():
                if key == "make":
                    filter_params["make__contains"] = val
                elif key == "model":
                    filter_params["model__contains"] = val
                elif key == "condition":
                    filter_params["condition__description__contains"] = val
                elif key == "price_min":
                    filter_params["price__gte"] = val
                elif key == "price_max":
                    filter_params["price__lte"] = val     
                elif key == "hours_min":
                    filter_params["hours__gte"] = val
                elif key == "hours_max":
                    filter_params["hours__lte"] = val     

            tractors = Tractor.objects.filter(** filter_params)
            ids = [t.id for t in tractors]
            equipments = Equipment.objects.filter(tractor__id__in=ids)
            
            equipment_dict = {} 
            for e in equipments:
                if (e.tractor_id not in equipment_dict):
                    equipment_dict[e.tractor_id] = []    
                equipment_dict[e.tractor_id].append(e.name)

            return JsonResponse(
                {                
                    "tractors" : [                
                        {
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
                            "equipment": equipment_dict[tractor.id] if tractor.id in equipment_dict else []
                        }
                        for tractor in tractors
                    ]
                }
            )

        except:
            return JsonResponse(
                {"error_code": 1},
                status=HTTPStatus.NOT_FOUND
            ) 


class Compare(View):
    def get(self, request):
        try:
            if ("tractors" not in request.GET):
                return JsonResponse(
                    {"error_code": 1},
                    status=HTTPStatus.NOT_FOUND
                )
                              
            tractors = Tractor.objects.filter(id__in=request.GET.getlist("tractors"))
            equipments = Equipment.objects.filter(tractor__id__in=request.GET.getlist("tractors"))
            equipment_dict = {} 
            for e in equipments:
                if (e.tractor_id not in equipment_dict):
                    equipment_dict[e.tractor_id] = []    
                equipment_dict[e.tractor_id].append(e.name)

            best_vals = {}
            for t in tractors:
                if t.price is not None and ("price" not in best_vals or t.price < best_vals["price"]):
                    best_vals["price"] = t.price
                if t.year is not None and ("year" not in best_vals or t.year > best_vals["year"]):
                    best_vals["year"] = t.year
                if t.hours is not None and ("hours" not in best_vals or t.hours < best_vals["hours"]):
                    best_vals["hours"] = t.hours
                if t.engine_power is not None and ("engine_power" not in best_vals or t.engine_power > best_vals["engine_power"]):
                    best_vals["engine_power"] = t.engine_power
                if t.documents_valid is not None and ("documents_valid" not in best_vals or t.documents_valid > best_vals["documents_valid"]):
                    best_vals["documents_valid"] = t.documents_valid
                
            return JsonResponse(
                {                
                    "tractors" : [              
                        {
                            "parameters" : {
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
                                "equipment": equipment_dict[tractor.id] if tractor.id in equipment_dict else []
                            },
                            "mark" : {
                                "price": True if "price" in best_vals and tractor.price == best_vals["price"] else False,
                                "year": True if "year" in best_vals and tractor.year == best_vals["year"] else False,
                                "hours": True if "hours" in best_vals and tractor.hours == best_vals["hours"] else False,
                                "engine_power": True if "engine_power" in best_vals and tractor.engine_power == best_vals["engine_power"] else False,
                                "documents_valid": True if "documents_valid" in best_vals and tractor.documents_valid == best_vals["documents_valid"] else False,
                            }
                        }
                        for tractor in tractors
                    ]
                }
            )

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