from django.db import models

class Patient(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    gender = models.CharField(max_length=10)
    room_number = models.CharField(max_length=10, null=True, blank=True)

    admitted_on = models.DateTimeField(auto_now_add=True)
    discharged_on = models.DateTimeField(null=True, blank=True)

    admission_status = models.CharField(
        max_length=20,
        choices=[
            ("ADMITTED","Admitted"),
            ("DISCHARGED","Discharged"),
            ("TRANSFERRED","Transferred"),
        ],
        default="ADMITTED"
    )
room_number = models.CharField(max_length=10, null=True, blank=True)
diagnosis = models.TextField(null=True, blank=True)

