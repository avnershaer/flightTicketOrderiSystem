from rest_framework import serializers
from ..dal import models
#import re
#import os
#from PIL import Image
from ..utils.validatorsView import GetValidations

validator = GetValidations()


# serializer for User Roles
class UserRoleSerializer(serializers.ModelSerializer, GetValidations):
    class Meta:
        model = models.UserRole
        fields = '__all__'
  

# serializer for Countries 
class CountriesSerializer(serializers.ModelSerializer, GetValidations):
    
    class Meta:
        model = models.Countries
        fields = ('country_name', 'country_id', 'country_flag')



# serializer for Airline Companies 
class AirlineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.AirLineCompanies
        fields = '__all__'


# serializer for Administrators
class AdministratorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Adminstrators
        fields = '__all__'
   

# serializer for Flights
class FlightsSerializer(serializers.ModelSerializer, GetValidations):

    origin_country_flag = CountriesSerializer(source='origin_country_id', read_only=True)
    destination_country_flag = CountriesSerializer(source='destination_country_id', read_only=True)
    air_line_name = AirlineSerializer(source='air_line_id', read_only=True)
    
    class Meta:
        model = models.Flights
        fields = ('flight_id', 'air_line_id', 'air_line_name', 'origin_country_flag', 'destination_country_flag', 'departure_time', 'landing_time', 'remaining_tickects')

# serializer for Flights
class CustomersSerializer(serializers.ModelSerializer, GetValidations):

    class Meta:
        model = models.Customers
        fields = '__all__'
        


# serializer for Tickets
class TicketsSerializer(serializers.ModelSerializer, GetValidations):

    # define relationships with related serializers
    customer = CustomersSerializer(source='cust_id', read_only=True)
    flight = FlightsSerializer(source='flight_id', read_only=True)


    class Meta:
        model = models.Tickets
        exclude = ['cust_id']


# serializer for Users
class UsersSerializer(serializers.ModelSerializer, GetValidations):

    class Meta:
        model = models.Users
        fields = '__all__'

   


  