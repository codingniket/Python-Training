# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
# @csrf_exempt
# def ok(request):
#     if request.method == "GET":
#         return JsonResponse({"message": "GETTING REQUEST"})
#     return HttpResponse("Checking")
#
# @csrf_exempt
# def welcome(request):
#     if request.method == "POST":
#         return JsonResponse({"message": "POST REQUEST"})
#     return HttpResponse("ok")
#
# @csrf_exempt
# def status(request):
#     if request.method == "PUT":
#         return JsonResponse({"message": "PUT REQUEST"})
#     return HttpResponse("ok")
#
# @csrf_exempt
# def dele(request):
#     if request.method == "DELETE":
#         return JsonResponse({"message": "DELETE REQUEST"})
#     return HttpResponse("ok")
#
# @api_view()
# def view_dtl(request):
#     return Response({'success': 409, 'message': 'api'})
#
# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def view_person(request):
#     if request.method == "GET":
#         return Response({"message": "GETTING REQUEST"})
#     elif request.method == "POST":
#         return Response({"message": "POST REQUEST"})
#     elif request.method == "PUT":
#         return Response({"message": "PUT REQUEST"})
#     elif request.method == "PATCH":
#         return Response({"message": "PATCH REQUEST"})
#     elif request.method == "DELETE":
#         return Response({"message": "DELETE REQUEST"})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
import json

@csrf_exempt
def employees(request):

    # GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(Employee.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Employee.objects.create(
            name=body["name"],
            role=body["role"],
            salary=body["salary"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        emp = Employee.objects.get(id=body["id"])
        emp.name = body["name"]
        emp.role = body["role"]
        emp.salary = body["salary"]
        emp.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        emp = Employee.objects.get(id=body["id"])
        emp.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
