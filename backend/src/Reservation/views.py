from django.shortcuts import render
from . import reservationService
from .models import Reservation
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def addReservation(request):
    print(request.GET.get('usrId'))
    try:
        responseData = {}
        data = reservationService.addReservation(request)
        if data is not None:
            responseData["Data"] = data
        else:
            responseData["Status"] = "Failed"
        return JsonResponse(responseData)

    except Exception as ex:
        print("[EXCEPTION] Add User Service : ")
        print(ex)
        responseData = {"Status": "Failed"}
        return JsonResponse(responseData)


def getReservationsForUser(request):
    try:

        responseData = reservationService.getReservationsForUser(request)
        return JsonResponse(responseData, safe=False)
    except Exception as ex:
        print("[EXCEPTION] Get All Reservations for User : ")
        print(ex)
        responseData = {"Status": "Failed"}
        return JsonResponse(responseData)

def getAllReservations(request):
    try:

        responseData = reservationService.getAllReservations(request)
        return JsonResponse(responseData, safe=False)
    except Exception as ex:
        print("[EXCEPTION] Get All Reservations for User : ")
        print(ex)
        responseData = {"Status": "Failed"}
        return JsonResponse(responseData)

def cancelReservation(request):
    try:
        responseData = reservationService.cancelReservation(request)
        return JsonResponse(responseData, safe=False)
    except Exception as ex:
        print("[EXCEPTION] Cancel Reservation : ")
        print(ex)
        responseData = {"Status": "Failed"}
        return JsonResponse(responseData)
