from .models import Reservation
from datetime import datetime
from TimeSlot.models import TimeSlot
from Area.models import Area
from Equipment.models import Equipment
from Sport.models import Sport
import traceback
from django.db.models import Q


def addReservation(request):
    try:
        reservationModel = Reservation()
        reservationModel.usrId = request.GET.get("usrId")
        reservationModel.areaId = request.GET.get("areaId")
        reservationModel.equipmentId = request.GET.get("equipmentId")
        reservationModel.sportId = request.GET.get("sportId")
        reservationModel.timeSlotId = request.GET.get("timeSlotId")
        reservationModel.reservationDate = datetime.now().date()
        reservationModel.save()

        return {"reservationId": reservationModel.reservationId}
    except Exception as ex:
        print(ex)
        return {"Status": "Failed"}


def getReservationsForUser(request):
    try:
        responseData = {}

        date = datetime.now().date()
        date_string = (date.strftime("%Y-%m-%d"))
        usrId = request.GET.get("usrId")
        reservationModel = Reservation.objects.all().values().filter(usrId=usrId, reservationDate=date_string)
        responseData["Reservations"] = list(reservationModel)

        for object in responseData["Reservations"]:
            sportId = object["sportId"]
            sportName = Sport.objects.all().values("sportName").filter(sportId=sportId)
            object["sportName"] = list(sportName)[0]["sportName"]
            areaId = object["areaId"]
            areaName = Area.objects.all().values("areaName").filter(areaId=areaId)
            object["areaName"] = list(areaName)[0]["areaName"]
            equipmentId = object["equipmentId"]
            equipmentName = Equipment.objects.all().values("equipmentName").filter(equipmentId=equipmentId)
            object["equipmentName"] = list(equipmentName)[0]["equipmentName"]
            timeSlotId = object["timeSlotId"]
            startTime = TimeSlot.objects.all().values("startTime").filter(timeSlotId=timeSlotId)
            object["startTime"] = list(startTime)[0]["startTime"]
            endTime = TimeSlot.objects.all().values("endTime").filter(timeSlotId=timeSlotId)
            object["endTime"] = list(endTime)[0]["endTime"]

        return responseData

    except Exception as ex:
        print(traceback.print_exc())
        responseData = {"Status": "Failed"}
        return responseData

def cancelReservation(request):
    try:
        reservationId = request.GET.get("reservationId")
        reservationModel = Reservation.objects.get(reservationId=reservationId)
        reservationModel.delete()
        responseData = {"Status": "Success", "reservationId": reservationId}
        return responseData
    except Exception as ex:
        print(traceback.print_exc())
        responseData = {"Status": "Failed"}
        return responseData