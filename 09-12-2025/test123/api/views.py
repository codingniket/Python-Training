from django.http import JsonResponse
def ok(request):
    return JsonResponse({"message": "Django API is working"})