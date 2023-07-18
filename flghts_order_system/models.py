from django.db import models
from django.core import validators


class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=25, unique=True)
    
    def __str__(self) -> str:
        return self.role_name

class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user_name

class Adminstrators(models.Model):
    admin_id = models.BigAutoField(primary_key=True)
    admin_first_name = models.CharField(max_length=100, blank=False, null=False, default='') 
    admin_last_name = models.CharField(max_length=100, blank=False, null=False, default='')
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.admin_first_name

class Customers(models.Model):
    cust_id = models.BigAutoField(primary_key=True)
    cust_first_name = models.CharField(max_length=100, blank=False, null=False)
    cust_last_name = models.CharField(max_length=100, blank=False, null=False)
    cust_adress = models.CharField(max_length=200)
    cust_phone_num = models.CharField(max_length=100, unique=True)
    cust_credit_card_num = models.CharField(unique=True, max_length=100)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.cust_first_name
    
class Countries(models.Model):
    country_id = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=200, blank=False, null=False)
    country_flag = models.ImageField(upload_to='images/countries_flags/', default='')    

    def __str__(self) -> str:
        return self.country_name

class AirLineCompanies(models.Model):
    air_line_id = models.BigAutoField(primary_key=True)
    air_line_name = models.CharField(max_length=100, unique=True)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    company_logo = models.ImageField(upload_to='images/companies_logos/', default='')

    def __str__(self) -> str:
        return self.air_line_name
    
class Flights(models.Model):
    flight_id = models.BigAutoField(primary_key=True)
    air_line_id = models.ForeignKey(AirLineCompanies, on_delete=models.CASCADE)
    origin_country_id = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='origin_flights')
    destination_country_id = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='destination_flights')
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    remaining_tickects = models.IntegerField()

    
class Tickets(models.Model):
    ticket_id = models.BigAutoField(primary_key=True)
    flight_id = models.ForeignKey(Flights, on_delete=models.CASCADE)
    cust_id = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f'customer - {self.cust_id} ticket -  {self.flight_id} ')
