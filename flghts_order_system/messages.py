from .loggers import *
from django.http import JsonResponse


logger = lggr()
errlogger = errLogger()


def error_405(request):
    errlogger.error(f'{request.method} METHOD NOT ALLOWD HTTP/1.1" 405' )
    msg =JsonResponse ({'status':'ERROR', 'details':f'405 -- {request.method} METHOD IS NOT ALLOWD'}, status=405)
    return msg

#def error_no_mach_id():
#    errlogger.error(
#        "maching query does not exist - cannot access local variable where it is not associated with a value"
#        )
#    msg = JsonResponse({
#        'status': 'ERROR', 
#        'error': "maching query does not exist - cannot access local variable where it is not associated with a value"
#        })
#    return msg           

def error_400(obj):
    errlogger.error(obj['error'])
    msg= JsonResponse({'status': 'ERROR', 'error': obj['error']}, status=400)
    return msg

def error_500(e, model):
    errlogger.error(e)
    msg =  JsonResponse({'status':f'ERROR at {model}', 'ERROR':str(e)}, status=500)
    return msg

def error_404(e, obj, model):
    errlogger.error(f'{obj} Not Found - model {model} got ERROR:{e} HTTP/1.1" 404')
    msg= JsonResponse({'status': 'ERROR', 'message': f'{obj} Not Found got ERROR:{e}'}, status=404)
    return msg

def ok_status_200(object, obj_name):
    logger.info(f'O.K for {obj_name}  HTTP/1.1" 200')
    return object 

def status_200_json(object, obj_name):
        logger.info(f'O.K got object/list HTTP/1.1" 200')
        return JsonResponse({obj_name: object}, status=200)

def ok_obj_from_db(object):
    logger.info(f'O.K got objects from database:{object} HTTP/1.1" 200')
    return object

def ok_status_201(object):
    logger.info('O.K New user been created HTTP/1.1" 201 ')
    msg = JsonResponse({'status': 'success', 'Datails': object}, status=201, safe=False)
    return msg

def got_request(request):
    msg =logger.info(f'{request.method} request received HTTP/1.1" 100')
    return msg

def got_serialized_valid_data():
    logger.info(f'O.K got user valid data - HTTP/1.1" 200')

def ok_status_204(object_id):
    logger.info(f'O.K object no.{object_id} been deleted - HTTP/1.1 204 No Content')
    msg = JsonResponse({
        'status':'success', 
        'Datails':f'O.K object no.{object_id} been deleted - HTTP/1.1 204 No Content'
        }, 
            status=201, 
            safe=False
            )
    return msg

def ok_move_to(model):
    msg =logger.info(f'ok move to {model} status HTTP/1.1 200')
    return msg

def ok_chek_error_is_false(model):
    msg =logger.info(f'ok check error at {model} is false. status HTTP/1.1 200')
    return msg