from django.shortcuts import render

# Create your views here.


class Ratings(View):
    def get(self, request, tractor_id, username):
        try:
            tractor_id = Tractors.

            return JsonResponse({
                "tractor_id": ratings.tractor_id,
                "username": ratings.username,
                "stars": ratings.stars,
                "comment": ratings.comment,
            })

        except:
            return JsonResponse(
                {"error_code": 1},
                status=HTTPStatus.NOT_FOUND
            )