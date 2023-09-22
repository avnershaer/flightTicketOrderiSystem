#from ..forms import UserRoleForm
from ..dal.models import *
#from django.shortcuts import HttpResponse
from ..dal.dalViews import Dal
from django.http import JsonResponse
#from ..Serializers import UsersSerializer
#from .. import models
#from rest_framework.parsers import JSONParser
from django.core import serializers
#from django.core.serializers import serialize
import json
#import re
from loggers import*
from ..utils.validatorsView import *
#from rest_framework.views import APIView
from ..utils.response_messages import *
from .Serializers import FlightsSerializer
#from django.utils import timezone
#from datetime import timedelta
#from ..validatorsView import GetValidations
from ..utils.operation_funcs import *
    
logger = lggr()
errlogger = errLogger()
dal = Dal()
validator = GetValidations()
flight_serializer = FlightsSerializer


# retrieve a list of objects from the database using the data access layer (dal)
def api_get_list(instance_model, model_serializer):
    ok_move_to(model='SysApiViews', func='api_get_list')
    
    try:
        # get a list of objects using the data access layer (dal)
        objects_list = dal.table_objects_list(model=instance_model)
        ok_got_back(view='dal', obj=objects_list)
        
        # check in no errors returned (FALSE)
        if validator.if_isinstance(objects_list) != False:

            # error response if error returned
            return check_error_true(model='SysApiViews', func='api_get_list', obj=objects_list)

        # no errors - serialize the data 
        obj_list = serialize_data(model_serializer=model_serializer, instance_model=instance_model, objects=objects_list, many=True)
        
        # return jsonresponse with object list
        return obj_list
    
    # handle any exceptions that occur during processing this method      
    except Exception as e:
        return error_500(e=e, model='SysApiViews')

# create new instance object using the data access layer (dal)
def api_Create_new(data, instance_model, model_serializer):
    ok_move_to(model='SysApiViews', func='api_Create_new()')
    
    try:
        # create the object using the data access layer (dal)
        new_obj = dal.create_new(**data, model=instance_model)
        ok_got_back(view='dal', obj=new_obj)
        
        # check in no errors returned (FALSE)
        if validator.if_isinstance(new_obj) !=False:

            # error response if error returned
            return new_obj

        # no errors
        # check if object contains user_id 
        if hasattr(new_obj, 'user_id'):
            
            # if contains user_id it means register process
            return new_obj
        
        # do not contains user_id, and no errors - serialize the data       
        details = serialize_data(model_serializer=model_serializer, instance_model=instance_model,objects=new_obj, many=False)
        ok_got_back(view='operation_funcs', obj=details)
        
        # return jsonresponse with new_obj 
        return details

    # handle any exceptions that occur during processing this method      
    except Exception as e:
        return error_500(e=e, model='SysApiViews')
       
# retrieve a list of object\s by id from the database, using the data access layer (dal)
def api_get_object_by_entity_id(id, instance_model, model_serializer, entity):
    ok_move_to(model='SysApiViews', func='api_get_list')
    
    try:
        # get a list of object\s by id using the data access layer (dal)
        obj = dal.get_object_by_entity_id(id=id, model=instance_model, entity=entity)
        ok_got_back(view='dal', obj=obj)
        
        # check if no errors returned (FALSE)
        if validator.if_isinstance(obj) != False:
            
            # error response if error returned
            return check_error_true(model='SysApiViews', func='api_get_object_by_entity_id', obj=obj)
        
        # no errors - check if one, multi or none object, and serialize the data or returning an error response.
        return check_one_multi_none(obj=obj, instance_model=instance_model, model_serializer=model_serializer)
       
    # handle any exceptions that occur during processing this method      
    except Exception as e:
        return error_500(e=e, model='SysApiViews')

# retrieve a list of flight object\s by date from the database, using the data access layer (dal)
def api_get_flights_by_date(instance_model, model_serializer, time_type, date):
    ok_move_to(model='SysApiViews', func='api_get_flights_by_date')
    
    try:
        # get from the database a list of flight object\s by date, by using the data access layer (dal)
        flights = dal.get_flights_by_date(model=instance_model, time_type=time_type)
        ok_got_back(view='dal', obj=flights)
        
        # check if no errors returned (FALSE)
        if validator.if_isinstance(flights) != False:
            
            # error response if error returned
            return flights
        
        # no errors - check if one, multi or none object, and serialize the data or returning an error response.
        return check_one_multi_none(obj=flights, instance_model=instance_model, model_serializer=model_serializer)

    # handle any exceptions that occur during processing this method      
    except Exception as e:
        return error_500(e=e, model='SysApiViews')
    
# retrieve a list of next 12 hours flights object\s, using the data access layer (dal)
def api_get_next_12_hours_flights(entity, model_serializer, instance_model, country_id, country_type):
    ok_move_to(model='SysApiViews', func='api_get_last_12_hours_flights')
    
    try:
        # get from the database a list of next 12 hours flights object\s, using the data access layer (dal)
        flights = dal.get_next_12_hours_flights(entity=entity, model=instance_model, country_id=country_id, country_type=country_type)
        
        # check if no errors returned (FALSE)
        if validator.if_isinstance(flights) != False:

            # error response if error returned
            return flights
        
        # no errors - check if one, multi or none object, and serialize the data or returning an error response.
        return check_one_multi_none(obj=flights, instance_model=instance_model, model_serializer=model_serializer)
    
    # handle any exceptions that occur during processing this method      
    except Exception as e:
        return error_500(e=e, model='SysApiViews')

# update instance object using the data access layer (dal)
def api_update_instance(validated_data, id, instance_model, model_serializer):
    ok_move_to(model='SysApiViews', func='api_update_instance')
    
    try:
        # update instance object using the data access layer (dal)
        updated_obj = dal.update(id=id, **validated_data, model=instance_model)
        ok_got_back(view='dal', obj='updated_obj')
      
        # check if no errors returned (FALSE)
        if validator.if_isinstance(updated_obj) != False:

            # error response if error returned
            return updated_obj

        # no errors - serialize the data       
        details = serialize_data(model_serializer=model_serializer, instance_model=instance_model,objects=updated_obj, many=True)
        
        # return jsonresponse with updated_obj 
        return details 

    # handle any exceptions that occur during processing this method      
    except Exception as e:
       return error_500(e=e, model='SysApiViews')
              
# delete object from database using the data access layer (dal)
def api_delete(id, instance_model):
    ok_move_to(model='API View', func='api_delete')
    
    try:
        # deleting the object
        deleted_object = dal.delete(model=instance_model, id=id)
        ok_got_back(view='dalView', obj='been removed')
        
        # success jsonresponse or an error jsonresponse 
        return deleted_object
    
    # handle any exceptions that occur during processing this method      
    except Exception as e:
        return error_500(e=e, model='SysApiView')

# retrieve an object by the username from the database (for login), using the data access layer (dal)
def api_get_object_by_username(name, instance_model, model_serializer):
    ok_move_to(model='SysApiViews', func='api_get_object_by_username')
    try:
        # get the object
        obj = dal.get_object_by_username(name=name, model=instance_model)
        ok_got_back(view='dal', obj=obj)
        
        
        # check if no errors returned (FALSE)
        if validator.if_isinstance(obj) != False:

            # error response if error returned
            return obj
        
        # no errors - serialize the object 
        serializer = model_serializer(obj)
        logger.info(f'O.K {obj} object been serialized HTTP/1.1" 200')
        
        # return the object for cuntinue login proccess
        return serializer.data

    # handle any exceptions that occur during processing this method      
    except Exception as e:
        return error_500(e=e, model='SysApiViews')

def api_get_object_by_user_id(model, model_serializer, user_id, ):
    ok_move_to(model='SysApiViews', func='api_get_object_by_user_id')
    try:
        # get the object
        obj = dal.get_object_by_user_id(model=model, user_id=user_id)
        ok_got_back(view='dal', obj=obj)
        
        # check if no errors returned (FALSE)
        if validator.if_isinstance(obj) != False:
            # error response if error returned
            return obj
        
        # no errors - serialize the object 
        user_id_object = serialize_data(instance_model=model, model_serializer=model_serializer, objects=obj, many=False)
        logger.info(f'O.K {user_id_object} object been serialized HTTP/1.1" 200')
        
        # return the object for cuntinue login proccess
        return user_id_object

    # handle any exceptions that occur during processing this method      
    except Exception as e:
        return error_500(e=e, model='SysApiViews')




def api_create_multi(validatedData, instance_model, model_serializer):
    multi_new_user_roles = []
    try:
        for data in validatedData:
            serializer = model_serializer(data=data)
            if serializer.is_valid():
                logger.info(f'O.K got user valid data')
                dal.model = instance_model
                new_obj = dal.create(**serializer.validated_data)
                if isinstance(new_obj, dict) and 'error' in new_obj:
                    errlogger.error(new_obj['error'])
                    return JsonResponse({'status': 'ERROR', 'error': new_obj['error']}, status=500)
                else:
                    logger.info(f'O.K created new object at {instance_model}')
                    multi_new_user_roles.append(new_obj)
            else:
                errors = serializer.errors
                return {'error': str(errors)}    
        serialized_new_user_roles = serializers.serialize('json', multi_new_user_roles)
        deserialized_user_roles = json.loads(serialized_new_user_roles)
        return deserialized_user_roles
    except Exception as e:
        return {'error': str(e)}

































































































