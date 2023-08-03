import re
import os
from .loggers import *
from django.http import JsonResponse
from rest_framework import serializers
from PIL import Image


errlogger = errLogger()
logger = lggr()



def check_if_None(data, model):
    if None in data.values():
        return True
    else:
        return False
    

class GetValidations:
    
    def validate_name(self, value):
        pattern = r'^[A-Za-z0-9_-]{3,}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Invalid data format:name must be onley A-Z a-z 0-9 _ - and <3 ltters - no spaces allowd")
        return value

    def validate_email(self, email):
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
        if not re.match(pattern, email):
            raise serializers.ValidationError("Invalid email format")
        return email

    def validate_password(self, password):
        pattern = r'^(?=.*\d)(?=.*[a-z]).{4,}$'
        if not re.match(pattern, password):
            raise serializers.ValidationError("Invalid password format: The password must contain at least one digit, one lowercase letter, and must be at least 4 characters long")
        return password

















    def validate_pic_image(self, value):

        try:
            image = Image.open(value)
        except IOError:
            raise serializers.ValidationError("Invalid image file.")
        allowed_types = ['image/jpeg', 'image/png', 'image/gif']
        max_size = 2 * 1024 * 1024  
        max_width = 1000
        max_height = 1000
        image_width, image_height = image.size
        allowed_characters = r'^[A-Za-z0-9_.-]+$'
        file_name = os.path.basename(value.name)
        if value.content_type not in allowed_types:
            raise serializers.ValidationError("Invalid file type. Allowed types: JPEG, PNG, GIF.")
        if value.size > max_size:
            raise serializers.ValidationError("File size exceeds the maximum limit (2MB).")
        if image_width > max_width or image_height > max_height:
            raise serializers.ValidationError("Image dimensions are too big - maximum limit 1000x1000.")
        if not re.match(allowed_characters, file_name):
            raise serializers.ValidationError("Invalid file name. A-z a-z, 0-9, - , _ , and . are allowed.")
        return value
    
    def validate_pic_image_no_pic_sizes(self, value):
        allowed_types = ['image/jpeg', 'image/png', 'image/gif']
        max_size = 2 * 1024 * 1024  
        allowed_characters = r'^[A-Za-z0-9_.-]+$'
        file_name = os.path.basename(value.name)
        if value.content_type not in allowed_types:
            raise serializers.ValidationError("Invalid file type. Allowed types: JPEG, PNG, GIF.")
        if value.size > max_size:
            raise serializers.ValidationError("File size exceeds the maximum limit (2MB).")
        if not re.match(allowed_characters, file_name):
            raise serializers.ValidationError("Invalid file name. A-z a-z, 0-9, - , _ , and . are allowed.")
        return value

    def if_isinstance(self, obj):
        if isinstance(obj, JsonResponse):
            return obj 
        else:
            return False