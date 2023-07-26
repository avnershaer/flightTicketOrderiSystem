from ..forms import UserRoleForm
from ..models import *
from django.shortcuts import HttpResponse
from .dalViews import Dal
from django.http import JsonResponse
from ..Serializers import UsersSerializer
from .. import models
from rest_framework.parsers import JSONParser
from django.core import serializers
from django.core.serializers import serialize
import json
import re
from ..loggers import*
from ..validatorsView import *
from rest_framework.views import APIView
from ..messages import *
from ..Serializers import FlightsSerializer
from django.utils import timezone
from datetime import timedelta
from ..validatorsView import GetValidations
from ..operation_funcs import *
    
logger = lggr()
errlogger = errLogger()
dal = Dal()
validator = GetValidations()
flight_serializer = FlightsSerializer




#def serialize_data2(model_serializer, objects, instance_model):
#    ok_move_to(model='**********', func='serialize_data2')
#    logger.info(f'O.K GOT objects HTTP/1.1 200 {instance_model}')
#    serializer = model_serializer(objects, many=True)
#    logger.info(f'O.K  objects BEEN SERIALIZED HTTP/1.1 200')
#    return serializer.data


def api_get_list(instance_model, model_serializer):
    ok_move_to(model='SysApiViews', func='api_get_list')
    try:
        objects_list = dal.table_objects_list(model=instance_model)
        ok_got_back(view='dal', obj=objects_list)
        check_error = validator.if_isinstance(objects_list) # check if no errors returned (FALSE)
        if check_error == False:
            ok_chek_error_is_false(model='SysApiViews')
            obj_list = serialize_data(model_serializer=model_serializer, instance_model=instance_model, objects=objects_list, many=True)
            return obj_list
        else:
            return check_error_true(model='SysApiViews', func='api_get_list', obj=objects_list)
    except Exception as e:
        return error_500(e=e, model='SysApiViews')

def api_Create_new(data, instance_model, model_serializer):
    ok_move_to(model='SysApiViews', func='api_Create_new')
    try:
        new_obj = dal.create_new(**data, model=instance_model)
        ok_got_back(view='dal', obj=new_obj) 
        check_error = validator.if_isinstance(new_obj) # check if no errors returned (FALSE)
        if check_error == False:
            ok_chek_error_is_false(model='SysApiViews')
            try:
                details = serialize_data(model_serializer=model_serializer, instance_model=instance_model,objects=new_obj, many=False)
                ok_got_back(view='operation_funcs', obj=details)
                return details
            except Exception as e:
                return check_error_true(model='SysApiViews', func='api_Create_new', obj=new_obj)
        else:
            return new_obj
    except Exception as e:
        return error_500(e=e, model='SysApiViews')
       
def api_get_object_by_entity_id(id, instance_model, model_serializer, entity):
    ok_move_to(model='SysApiViews', func='api_get_list')
    try:
        obj = dal.get_object_by_entity_id(id=id, model=instance_model, entity=entity)
        ok_got_back(view='dal', obj=obj)
        check_error = validator.if_isinstance(obj) # check if no errors returned (FALSE)
        if check_error == False:
            ok_chek_error_is_false(model='SysApiViews')
            return check_one_multi_none(obj=obj, instance_model=instance_model, model_serializer=model_serializer)
        else:
            return check_error_true(model='SysApiViews', func='api_get_object_by_entity_id', obj=obj)
    except Exception as e:
        return error_500(e=e, model='SysApiViews')

def api_get_flights_by_date(date, instance_model, model_serializer, time_type):
    ok_move_to(model='SysApiViews', func='api_get_flights_by_date')
    try:
        flights = dal.get_flights_by_date(date=date, model=instance_model, time_type=time_type)
        ok_got_back(view='dal', obj=flights)
        check_error = validator.if_isinstance(flights) # check if no errors returned (FALSE)
        if check_error == False:
            ok_chek_error_is_false(model='SysApiViews')
            return check_one_multi_none(obj=flights, instance_model=instance_model, model_serializer=model_serializer)
        else:
            return check_error_true(model='SysApiViews', func='api_get_object_by_entity_id', obj=flights)
    except Exception as e:
        return error_500(e=e, model='SysApiViews')
    
def api_get_next_12_hours_flights(entity, model_serializer, instance_model, country_id, country_type):
    ok_move_to(model='SysApiViews', func='api_get_last_12_hours_flights')
    try:
        flights = dal.get_next_12_hours_flights(entity=entity, model=instance_model, country_id=country_id, country_type=country_type)
        check_error = validator.if_isinstance(flights)
        if check_error == False:
            ok_chek_error_is_false(model='SysApiViews')
            return check_one_multi_none(obj=flights, instance_model=instance_model, model_serializer=model_serializer)
        else:
            return check_error_true(model='SysApiViews', func='api_get_last_12_hours_flights', obj=flights)
    except Exception as e:
        return error_500(e=e, model='SysApiViews')
 
def api_update_instance(validated_data, id, instance_model, model_serializer):
    ok_move_to(model='SysApiViews', func='api_update_instance')
    try:
        #dal.model = instance_model
        updated_obj = dal.update(id=id, **validated_data, model=instance_model)
        ok_got_back(view='dal', obj='updated_obj')
        check_error = validator.if_isinstance(updated_obj)
        if check_error == False:
            ok_chek_error_is_false(model='SysApiViews')
            try:
                details = serialize_data(model_serializer=model_serializer, instance_model=instance_model,objects=updated_obj, many=True)
                ok_got_back(view='operation_funcs', obj=details)
                return details 
            except Exception as e:
                return check_error_true(model='SysApiViews', func='api_Create_new', obj=updated_obj)
        else:
            return updated_obj
    except Exception as e:
       return error_500(e=e, model='SysApiViews')
              
def api_delete(id, instance_model):
    ok_move_to(model='API View', func='api_delete')
    try:
        deleted_object = dal.delete(model=instance_model, id=id)
        ok_got_back(view='dalView', obj='been removed')
        return  deleted_object
    except Exception as e:
        return error_500(e=e, model='SysApiView')














































































def api_cccCreate_new(validatedData, instance_model, model_serializer):
    try:
        serializer = model_serializer(data=validatedData)
        if serializer.is_valid():
            logger.info(f'O.K got user valid data')
            dal.model = instance_model
            new_obj = dal.create(**serializer.validated_data)
            if isinstance(new_obj, dict) and 'error' in new_obj:
                errlogger.error(new_obj['error'])
                return JsonResponse({'status': 'ERROR', 'error': new_obj['error']}, status=500)
            else:
                logger.info(f'O.K created new object at {instance_model}')
                serialized_new_obj = model_serializer(new_obj).data
                logger.info(f'O.K {instance_model} object been serialized ')
                return  serialized_new_obj
        else:
            errors = serializer.errors
            return {'error': str(errors)}
    except Exception as e:
        return {'error': str(e)}



























def api_get_by_id(id, instance_model, model_serializer):
    try:
        obj = dal.getById(instance_model, id)
        if isinstance(obj, dict) and 'error' in obj:
                errlogger.error(obj['error'])
                return JsonResponse({'status': 'ERROR views', 'error': obj['error']}, status=500)
        else:
            logger.info(f'O.K got {instance_model} object from db')
            serialized_obj = model_serializer(obj).data
            logger.info(f'O.K {instance_model} object been serialized ')
            return serialized_obj
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
        
def api_get_object_by_username(name, instance_model, model_serializer):
    try:
        obj = dal.get_object_by_username(name=name, model=instance_model)
        if isinstance(obj, JsonResponse) and "ERROR" in obj.content.decode("utf-8"):
            return obj
        else:
            logger.info(f'O.K got obj : {obj} HTTP/1.1" 200')
            serializer = model_serializer(obj)
            logger.info(f'O.K {obj} object been serialized HTTP/1.1" 200')
            return serializer.data
    except Exception as e:
        return error_500(e=e, model='SysApiViews')
        




#def api_flight_by_origin_country_id(origin_country_id):
#    try:
#        obj = dal.flights_by_origin_id(
#            id=origin_country_id,
#            )
#        if 'ERROR' in obj:
#            return obj
#        else:
#            logger.info(f'O.K got obj : {obj} HTTP/1.1" 200  ')
#            serializer = FlightsSerializer(obj, many=True)
#            serialized_data = serializer.data
#            logger.info(f'O.K {obj} object been serialized  HTTP/1.1" 200')
#            return serialized_data
#    except Exception as e:
#        return {'ERROR-API': str(e)}







  #serializer = model_serializer({'name':name})
    



#def api_get_customer_by_username(username, instance_model, model_serializer):
#    try:
#        obj = dal.get_customer_by_username(
#            username=username, 
#            model=instance_model, 
#            users=Users
#            )
#        if isinstance(obj, JsonResponse) and "ERROR" in obj.content.decode("utf-8"):
#            return obj
#        else:
#            logger.info(f'O.K got obj : {obj} HTTP/1.1" 200')
#            serializer = model_serializer(obj, many=True)
#            logger.info(f'O.K {obj} object been serialized HTTP/1.1" 200')
#            return serializer.data
#    except Exception as e:
#        return error_500(e=e, model='SysApiViews')












#def apiCreateNewUserRole(validatedData):    
#    try:
#        serializer = UserRoleSerializer(data=validatedData)
#        if serializer.is_valid():
#            dal.model = models.UserRole
#            newRole = dal.create(**serializer.validated_data)
#            serialized_newUserRole = UserRoleSerializer(newRole).data
#            return serialized_newUserRole
#        else:
#            errors = serializer.errors
#            return errors
#    except Exception as e:
#        return e
#
#def addNewUserRole(request):
#    form = UserRoleForm(request.POST)
#    try:
#        if form.is_valid():
#            roleName = form.cleaned_data['roleName']
#            Dal.model = UserRole
#            dal.create(roleName=roleName)
#            return HttpResponse('ok')
#    except Exception as e:
#        return HttpResponse(f'Error: {str(e)}')
#        
#def getUserRoleList():
#    dal = Dal()
#    dal.model = UserRole
#    roleList = dal.tableObjectsList(dal.model)
#    return roleList
#
#
#
#
#
#def apiGetUserRoleList():
#    try:
#        userRoleList = UserRole.objects.all()
#        logger.info('O.K got userRole objects from db ')
#        serializer = UserRoleSerializer(userRoleList, many=True)
#        logger.info('O.K got userRole objects serialized ')
#        return serializer.data
#    except Exception as e:
#        return e
#    
#
#
#
#
#
#
#
#
#
#
#def apiCreateNewUserRoles(validatedData):
#    newUserRoles = []
#    for data in validatedData:
#        serializer = UserRoleSerializer(data=data)
#        if serializer.is_valid():
#            dal.model = models.UserRole
#            newRole = dal.create(**serializer.validated_data)
#            #serialized_newUserRoles = UserRoleSerializer(newRole, many=True).data
#            newUserRoles.append(newRole)
#    serialized_user_roles = serializers.serialize('json', newUserRoles)
#    deserialized_user_roles = json.loads(serialized_user_roles)
#    return deserialized_user_roles
#
#def apiGetUserRoleById(id):
#    userRole = dal.getById(models.UserRole, id)
#    serialized_user_role = UserRoleSerializer(userRole).data
#    return serialized_user_role
#
#
#def apiDeleteUserRole(id):
#    userRole = dal.getById(models.UserRole, id)
#    try:
#        if userRole:
#            deletedObject = dal.delete(model=UserRole, id=id)
#            return deletedObject
#    except Exception as e:
#        return e