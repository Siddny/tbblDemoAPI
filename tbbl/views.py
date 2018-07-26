from django.shortcuts import render

from rest_framework import ( generics, status)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

import csv
import json

from django.http import HttpResponse

# from sendgrid.message import SendGridEmailMessage
from django.core.mail import send_mail

from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
import africastalking

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
			subject = 'Test subject'
			# if the org is regestering themselves the org id will alway be zero
			message = 'test email message'
			# invitation sent to organization
			mail_sent_to_org = send_mail(
				subject,
				message,
				"sidneykipronoh@gmail.com",
				[client.email]### TODO:
			)
		except Exception as e:
		  return Response(data={"Error":str(e)}, status = status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)
		

  # def get(self, request, format=None):
  #   try:
  #     scripts = Script.objects.all()
  #   except Exception as e:
  #     return Response(e, status = status.HTTP_400_BAD_REQUEST)
  #   return Response(data=scripts.values(), status = status.HTTP_200_OK)

class ClientsView(APIView):
	"""
	{
		"name": "sidney kiprono",
		"email": "mail@mail.com",
		"phone": "+254700021447"
	}
	"""
	def get(self, request, format=None):
		try:
			clients = Client.objects.all().values()
		except Exception as e:
			return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
		return Response(data=clients, status = status.HTTP_200_OK)

	def post(self, request, format=None):
		print(request.data)
		try:
			client = Client.objects.create(
				name = request.data['name'],
				email = request.data['email'],
				phone = request.data['phone']
				)
		except Exception as e:
			return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
		try:
			subject = 'Test subject'
			# if the org is regestering themselves the org id will alway be zero
			message = 'test email message'
			# invitation sent to organization
			mail_sent_to_org = send_mail(
				subject,
				message,
				"sidneykipronoh@gmail.com",
				['cdohzangah@gmail.com']### TODO:
			)
		except Exception as e:
			return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)

		try:
			username = "sandbox"    
			api_key = "bda966b554f93447c629953953c3a362f0fe21bb922943ba234f25f61435c56b"
			africastalking.initialize(username, api_key)
			sms = africastalking.SMS
			response = sms.send("Hello Message!", ["+254700021447"])
			print(response)

		except Exception as e:
			return Response(data={"Error 2":str(e)}, status = status.HTTP_400_BAD_REQUEST)

		return Response(status=status.HTTP_201_CREATED)
		# return Response(data=client, status=status.HTTP_201_CREATED)