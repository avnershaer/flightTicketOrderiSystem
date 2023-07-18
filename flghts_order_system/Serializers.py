from rest_framework import serializers
from . import models
import re
import os
from PIL import Image
from .validatorsView import GetValidations

validator = GetValidations()


class UserRoleSerializer(serializers.ModelSerializer, GetValidations):
    class Meta:
        model = models.UserRole
        fields = ['role_id', 'role_name', 'role_logo']

    #def validate_role_name(self, value):
    #    return self.validate_name(value)

    #def validate_role_logo(self, value):
    #    return self.validate_pic_image(value)   
   
class CountriesSerializer(serializers.ModelSerializer, GetValidations):
    
    class Meta:
        model = models.Countries
        fields = ['country_id', 'country_name', 'country_flag']

class AirlineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.AirLineCompanies
        fields = '__all__'

class AdministratorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Adminstrators
        fields = '__all__'
   
class FlightsSerializer(serializers.ModelSerializer, GetValidations):

    class Meta:
        model = models.Flights
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer, GetValidations):

    class Meta:
        model = models.Customers
        fields = '__all__'


class TicketsSerializer(serializers.ModelSerializer, GetValidations):

    class Meta:
        model = models.Tickets
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer, GetValidations):

    class Meta:
        model = models.Users
        fields = '__all__'


    def validate(self, data):
        validated_data = super().validate(data)
        validations = GetValidations()
        if 'user_name' in validated_data:
            validations.validate_name(validated_data['user_name'])
        if 'email' in validated_data:
            validations.validate_email(validated_data['email'])
        if 'password' in validated_data:
            validations.validate_password(validated_data['password'])
        return validated_data
    

   #def validate_user_name(self, value):
   #    return self.validate_name(value)
   #
   #def validate_user_email(self, value):
   #    return self.validate_email(value)

   #def validate_user_password(self, value):
   #    return self.validate_password(value)









    #ef validate_role_logo(self, value):
    #   try:
    #       image = Image.open(value)
    #   except IOError:
    #       raise serializers.ValidationError("Invalid image file.")
    #   allowed_types = ['image/jpeg', 'image/png', 'image/gif']
    #   max_size = 2 * 1024 * 1024  
    #   max_width = 1000
    #   max_height = 1000
    #   image_width, image_height = image.size
    #   allowed_characters = r'^[A-Za-z0-9_.-]+$'
    #   file_name = os.path.basename(value.name)
    #   if value.content_type not in allowed_types:
    #       raise serializers.ValidationError("Invalid file type. Allowed types: JPEG, PNG, GIF.")
    #   if value.size > max_size:
    #       raise serializers.ValidationError("File size exceeds the maximum limit (2MB).")
    #   if image_width > max_width or image_height > max_height:
    #       raise serializers.ValidationError("Image dimensions are too big - maximum limit 1000x1000.")
    #   if not re.match(allowed_characters, file_name):
    #       raise serializers.ValidationError("Invalid file name. A-z a-z, 0-9, - , _ , and . are allowed.")
    #   return value



















    #def validate_field_to_validate(self, value):
    #    pattern = r'^[A-Za-z0-9_-]{3,}$'
    #    if not re.match(pattern, value):
    #        raise serializers.ValidationError('Invalid data format')
    #    return value
    