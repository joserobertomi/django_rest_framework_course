from django.http import JsonResponse


def api_home(request, *args, **kargs):
    return JsonResponse({"message": "hey there this is an massage in the bottle!!"})
