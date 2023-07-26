from .loggers import *
from django.http import JsonResponse


logger = lggr()
errlogger = errLogger()


def error_405(request):
    errlogger.error(f'{request.method} METHOD NOT ALLOWD HTTP/1.1 405' )
    msg =JsonResponse ({'status':'ERROR', 'details':f'405 -- {request.method} METHOD IS NOT ALLOWD'}, status=405)
    return msg

def error_404(e, obj, model):
    errlogger.error(f'{obj} - model {model} got ERROR:{e} NOT FOUND HTTP/1.1 404')
    msg= JsonResponse({'status': 'ERROR NOT FOUND HTTP/1.1 404', 'datails': f'{obj} got ERROR:{e}'}, status=404)
    return msg

def dal_error(e):
    errlogger.error(f'DAL ERROR HTTP/1.1 500 - {e}')
    msg = JsonResponse({'DAL ERROR HTTP/1.1 500': str(e)}, status=500)
    return msg

def error_500(e, model):
    errlogger.error(e)
    msg =  JsonResponse({'status':f'ERROR at {model}', 'ERROR status HTTP/1.1 500':str(e)}, status=500)
    return msg

def ok_got_back(view, obj):
    info = logger.info(f'OK returned from {view} view.- object:{obj} HTTP/1.1 200')
    return info

def ok_move_to(model, func):
    msg =logger.info(f'O.K move to {model} model -function {func} status HTTP/1.1 200')
    return msg

def ok_obj_from_db(obj):
    logger.info(f'O.K got objects from database:{obj} HTTP/1.1 200')
    return obj

def ok_status_200(obj, obj_name):
    logger.info(f'O.K for {obj_name}  HTTP/1.1 200')
    return obj

def ok_chek_error_is_false(model):
    logger.info(f'O.K check error at {model} is FALSE. status HTTP/1.1 200')
    

def check_error_true(model, func, obj):
    errlogger.error(f'ERROR: check_error=TRUE at {model} - func {func} obj {obj}.--returning error_jsonResponse- - HTTP/1.1 500')
    return obj

def ok_status_201(obj, model):
    logger.info(f'O.K new instance BEEN CREATED: {obj} at model {model} - HTTP/1.1 201')
    return obj

def ok_got_serialzed_data(serialized_data):
    logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1 200')

def serialzed_data_is_valid():
    logger.info(f'O.K serialized data IS VALID HTTP/1.1 200')

def serialzed_data_NOT_valid(obj):
    logger.info(f'serialized data IS NOT VALID HTTP/1.1 500')
    msg = JsonResponse({'status':f'ERROR', 'details':obj}, status=500)
    return msg

def success_jsonResponse(obj):
    logger.info(f'O.K returning success_jsonResponse HTTP/1.1 200')
    msg = JsonResponse({'status': 'success O.K HTTP/1.1 200', 'Details': obj}, status=201, safe=False)
    return msg

def ok_vlidate_data(model, func):
    logger.info(f'OK GOT VALIDATE data at model:{model} - func:{func} status HTTP/1.1 200')













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






def status_200_json(object, obj_name):
        logger.info(f'O.K got object/list HTTP/1.1" 200')
        return JsonResponse({obj_name: object}, status=200)





def got_request(request):###
    msg =logger.info(f'{request.method} request received HTTP/1.1" 100')
    return msg

def got_serialized_valid_data():
    logger.info(f'O.K got user valid data - HTTP/1.1" 200')

def ok_status_204(object_id):
    logger.info(f'O.K object no.{object_id} been deleted - HTTP/1.1 204 No Content')
    msg = JsonResponse({'status':'success', 'Datails':f'O.K object no.{object_id} been deleted - HTTP/1.1 204 No Content' }, status=201, safe=False)
    return msg


