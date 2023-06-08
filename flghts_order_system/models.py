from django.db import models
from django.core import validators


class UserRole(models.Model):
    roleId = models.AutoField(primary_key=True)
    roleName = models.TextField(max_length=25, unique=True)
    


class Users(models.Model):
    userId = models.BigAutoField(primary_key=True)
    userName = models.TextField(max_length=100, unique=True)
    password = models.TextField(max_length=100)
    email = models.TextField(max_length=200, unique=True)
    userRole = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    

class Adminstrators(models.Model):
    adminId = models.BigAutoField(primary_key=True)
    adminFirstNmae: models.TextField(max_length=100) 
    adminLastNmae: models.TextField(max_length=100)
    userId = models.OneToOneField(Users, on_delete=models.CASCADE)
    adminPic = models.ImageField(upload_to='images/usersPics/')


class Customers(models.Model):
    custId = models.BigAutoField(primary_key=True)
    custFirstName = models.TextField(max_length=100)
    custLastName = models.TextField(max_length=100)
    custAdress = models.TextField(max_length=200)
    custPhoneNum = models.TextField(max_length=100, unique=True)
    custCreditCardNum = models.TextField(unique=True, max_length=100)
    userId = models.OneToOneField(Users, on_delete=models.CASCADE)
    custPic = models.ImageField(upload_to='images/usersPics/')    


class AirLineCompanies(models.Model):
    airLineId = models.BigAutoField(primary_key=True)
    airLineName = models.TextField(max_length=100, unique=True)
    countryId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    userId = models.OneToOneField(Users, on_delete=models.CASCADE)
    companyLogo = models.ImageField(upload_to='images/usersPics/')


class Countries(models.Model):
    CountryId = models.BigAutoField(primary_key=True)
    CountryName = models.TextField(max_length=200)


class Flights(models.Model):
    flightId = models.BigAutoField(primary_key=True)
    airLineId = models.ForeignKey(AirLineCompanies, on_delete=models.CASCADE)
    originCountryId = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='origin_flights')
    destinationCountryId = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='destination_flights')
    departureTime = models.DateTimeField()
    landingTime = models.DateTimeField()
    remainingTickects = models.IntegerField()

class Tickets(models.Model):
    ticketId = models.BigAutoField(primary_key=True)
    flightId = models.ForeignKey(Flights, on_delete=models.CASCADE)
    custId = models.ForeignKey(Customers, on_delete=models.CASCADE)
