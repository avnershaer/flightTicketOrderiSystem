from .Serializers import *
from .messages import *

def serialize_data(instance_model, model_serializer, objects, many):
    ok_move_to(model='operation_funcs', func='serialize_data')
    try:
        if objects:
            logger.info(f'O.K GOT objects HTTP/1.1 200 {instance_model}')
            serializer = model_serializer(objects, many=many)
            logger.info(f'O.K  objects BEEN SERIALIZED HTTP/1.1 200')
            return success_jsonResponse(obj=serializer.data)
        else:
            return serialzed_data_NOT_valid(obj=objects)
    except Exception as e:
        return error_500(e, model='operation_funcs')
 
def check_one_multi_none(obj, instance_model, model_serializer):
    ok_move_to(model='operation_funcs', func=f'check_one_multi_none--------------{obj}')
    if obj == None: # if there is no objects
        errlogger.error(f'ERROR: NOT FOUNT HTTP/1.1 404 - got None object from database ')
        msg = JsonResponse({'status':f'HTTP/1.1 404 NOT FOUND', 'details':'got None object from DATABASE'}, status=500)
        return msg
    elif isinstance(obj, instance_model): #if there is one object
        logger.info(f'O.K got one object from database HTTP/1.1 200')
        sobj = serialize_data(model_serializer=model_serializer, instance_model=instance_model, objects=obj, many=False)
        ok_got_back(view='operation_funcs', obj=sobj)
        return sobj
    elif len(obj) > 1: # if there is more then one object (list with 2 objects and more
        logger.info(f'O.K got multiple objects from database HTTP/1.1 200')
        sobj = serialize_data(model_serializer=model_serializer, instance_model=instance_model, objects=obj, many=True)
        ok_got_back(view='operation_funcs', obj=sobj)
        return sobj
    #else: #if there is no objects 
    #    errlogger.error(f'ERROR: NOT FOUNT HTTP/1.1 404 - got None object from database ')
    #    msg = JsonResponse({'status':f'HTTP/1.1 500 NOT FOUND', 'details':'got None object from DATABASE'}, status=500)
    #    return msg

def check_if_db_instance_one_multi_none(instance):
    ok_move_to(model='operation_funcs', func='check_if_db_instance_one_multi_none')
    if len(instance) == 0: # if no object found, return None
        errlogger.error(f'ERROR: NOT FOUNT HTTP/1.1 404 - got None object from database ')
        return None
    elif len(instance) == 1: # if only one object found, return object
        logger.info(f'O.K got one object from database HTTP/1.1 200')
        return ok_obj_from_db(obj=instance.first())
    else: # if multiple objects found return list of objects
        logger.info(f'O.K got multiple objects from database HTTP/1.1 200')
        return ok_obj_from_db(obj=instance)














#def serialize_data1(instance_model, model_serializer, objects):
#    ok_move_to(model='operation_funcs', func='serialize_data1')
#    logger.info(f'O.K got {str(instance_model)} objects list from db ')
#    serializer = model_serializer(objects)
#    logger.info(f'O.K {instance_model} objects been serialized ')
#    return serializer.data
# 
#flight_serializer = FlightsSerializer()   

#def data_serialize(data, serializer):
#    ok_move_to(model='operation_funcs', func='data_serialize')
#    try:
#        serialized_data = FlightsSerializer(data=data)
#        if serialized_data.is_valid():
#            serialzed_data_is_valid() 
#            return serialized_data
#        else:
#            return serialzed_data_NOT_valid(obj=serialized_data.errors)   
#    except Exception as e:
#        return error_500(e=e, model='AirLinesFacade')