from django.shortcuts import render
import json
from .models import Equipment
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
def getAllEquipments(request):
    try:
        # projects = Model.objects.all().values().filter(prjId=prjId)
        responseData = {}
        equiments=Equipment.objects.all().values().filter(sportId=request.GET.get("sportId"))
        equiments_list=list(equiments)
        if len(equiments_list) > 0:
            responseData["Equipment"] = equiments_list
            return responseData
        else:
            return None

    except Exception as ex:
        print(ex)
        data = {}
        data["Status"] = "Failed"
        return data