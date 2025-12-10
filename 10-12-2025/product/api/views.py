from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products
import json

@csrf_exempt
def product(request):

    # GET ALL product
    if request.method == "GET":
        data = list(Products.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Products.objects.create(
            name=body["name"],
            description=body["description"],
            price=body["price"],
            date=body["mfdate"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE Products (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        emp = Products.objects.get(id=body["id"])
        emp.name=body["name"],
        emp.description=body["description"],
        emp.price=body["price"],
        emp.date=body["mfdate"]
        emp.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE Products (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        emp = Products.objects.get(id=body["id"])
        emp.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
