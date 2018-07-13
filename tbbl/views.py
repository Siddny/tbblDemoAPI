from django.shortcuts import render

from rest_framework import ( generics, status)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

import csv
import json

from django.http import HttpResponse

# Create your views here.

class CsvScriptsView(APIView):

	def get(self, request, format=None):
		try:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="telescript.csv"'
			scripts = Script.objects.all().values()

			# x = json.loads(list(scripts))

			writer = csv.writer(response)

			# Write CSV Header, If you dont need that, remove this line
			# f = csv.writer(open("test.csv", "wb+"))
			writer.writerow(["id", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "dispose", "othersystems", "timetocall"])

			for x in scripts:
			    writer.writerow([x["id"],
			                x["q1"],
			                x["q2"],
			                x["q3"],
			                x["q4"],
			                x["q5"],
			                x["q6"],
			                x["q7"],
			                x["q8"],
			                x["q9"],
			                x["q10"],
			                x["q11"],
			                x["dispose"],
			                x["othersystems"],
			                x["timetocall"],
			                ])
			return response
		except Exception as e:
			return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
		return Response(data=scripts, status = status.HTTP_200_OK)


class ScriptView(APIView):

  def post(self, request, format=None):
    """
    {
        "q1": "",
        "q2": "",
        "q3": "",
        "q4": "",
        "q5": "",
        "q6": "",
        "q7": "",
        "q8": "",
        "q9": "",
        "q10": "",
        "q11": "",
		"dispose": "",
		"othersystems": "",
		"timetocall": ""
    }
    """
    print(request.data)
    try:
        script = Script.objects.create( **request.data)
    except Exception as e:
      return Response(data={"Error":str(e)}, status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

  # def get(self, request, format=None):
  #   try:
  #     scripts = Script.objects.all()
  #   except Exception as e:
  #     return Response(e, status = status.HTTP_400_BAD_REQUEST)
  #   return Response(data=scripts.values(), status = status.HTTP_200_OK)