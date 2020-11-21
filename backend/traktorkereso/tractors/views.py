from django.shortcuts import render

# Create your views here.


class Rating(View):
    def get(self, request, tractor_id, username):
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