from loggers.loggers import errLogger
from django.http import JsonResponse

errlogger = errLogger()


# if check_error is true generates a 500 error response
def check_error_true(model, func, obj):
    errlogger.error(f'ERROR: check_error=TRUE at {model} - func {func} obj {obj}.--returning error_jsonResponse- - HTTP/1.1 500')
    return obj

# generates 405 error response
def error_405(request):
    errlogger.error(f'{request.method} METHOD NOT ALLOWD HTTP/1.1 405' )
    msg =JsonResponse ({'status':'ERROR', 'details':f'405 -- {request.method} METHOD IS NOT ALLOWD'}, status=405)
    return msg

# generates 404 error response
def error_404(e, obj, model, oid):
    errlogger.error(f'{obj} - model {model} got ERROR:{e} NOT FOUND HTTP/1.1 404')
    msg = JsonResponse({'status': 'ERROR NOT FOUND HTTP/1.1 404', 'error': f'{obj}:{oid} =>  ERROR NOT FOUND HTTP/1.1 404 '}, status=404)
    return msg

# generates 403 error response
def error_403(e=''):
    errlogger.error(f'Forbidden - Unauthorized access  {e} - HTTP/1.1  403 ')
    msg = JsonResponse({'error': f'Unauthorized access {e} - HTTP/1.1  403'}, status=403)
    return msg

# generates DAL error response
def dal_error(e):
    errlogger.error(f'DAL ERROR HTTP/1.1 500 - {e}')
    msg = JsonResponse({'error':f'DAL ERROR HTTP/1.1 500---{str(e)}','details':f':{str(e)}'}, status=500)
    return msg

# generates 500 error response
def error_500(e, model):
    errlogger.error(e)
    msg =  JsonResponse({'status':f'{model}  got ERROR {str(e)} HTTP/1.1 500', 'details':f':{str(e)}'}, status=500)
    return msg

# generates message when object is not created successfully
def error_not_created(obj):
    errlogger.error(f'{obj} DID NOT CREATED, deleting the new user... HTTP/1.1 500' )

# generates 409 error response for already logged in user
def already_logged_in():
    errlogger.error('USER ALREADY LOGGED IN - HTTP/1.1 409' )
    msg = JsonResponse({'status':'user is already logged in HTTP/1.1 409'}, status=409)
    return msg

# generates 401 error response for an active session
def session_is_active_json(state):
    errlogger.error(f'session is {state} active')
    msg = JsonResponse(f'session is {state} active - HTTP/1.1 401 Unauthorized', safe=False, status=401)
    return msg

# generates message with error 400 if error check returns not true
def error_is_not_true(obj, obj_name):
    errlogger.error(f'ERROR:Invalid data - {obj_name}: {obj} is not True --HTTP/1.1 400')
    return obj

# generates 401 error response for authentication failure
def auth_failed():
    errlogger.error('Authentication failed - invalid credentials HTTP/1.1 401')
    msg = JsonResponse({'error':'Invalid credentials HTTP/1.1 401 Authentication failed '}, status=401)
    return msg

# generates 401 error response when serialized data is not valid
def serialzed_data_NOT_valid(obj):
    errlogger.error(f'serialized data IS NOT VALID HTTP/1.1 500')
    msg = JsonResponse({'status':f'ERROR', 'details':obj}, status=500)
    return msg



