from django.db import models

# Create your models here.
class Client(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	phone = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		db_table = "Client"
		verbose_name = "Client"
		verbose_name_plural = "Clients"

class Script(models.Model):
	q1 = models.CharField(max_length=100, null=True, blank=True)
	q2 = models.CharField(max_length=100, null=True, blank=True)
	q3 = models.CharField(max_length=100, null=True, blank=True)
	q4 = models.CharField(max_length=100, null=True, blank=True)
	q5 = models.CharField(max_length=100, null=True, blank=True)
	q6 = models.CharField(max_length=100, null=True, blank=True)
	q7 = models.CharField(max_length=100, null=True, blank=True)
	q8 = models.CharField(max_length=100, null=True, blank=True)
	q9 = models.CharField(max_length=100, null=True, blank=True)
	q10 = models.CharField(max_length=100, null=True, blank=True)
	q11 = models.CharField(max_length=100, null=True, blank=True)
	dispose = models.CharField(max_length=100, null=True, blank=True)
	othersystems = models.CharField(max_length=100, null=True, blank=True)
	timetocall = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		db_table = "Script"
		verbose_name = "Script"
		verbose_name_plural = "Scripts"

	# def __str__ (self):
	# 	return self.q1


