from loggers.loggers import *
from django.http import JsonResponse



logger = lggr()
errlogger = errLogger()


# generates info log when returned from last func
def ok_got_back(view, obj):
    info = logger.info(f'OK returned from {view} view.- object:{obj} HTTP/1.1 200 OK')
    return info

# generates info log when moving to another function
def ok_move_to(model, func):
    logger.info(f'O.K move to {model} model -function {func} status HTTP/1.1 200 OK')
    
# generates info log when objects are fetched from the database
def ok_obj_from_db(obj):
    logger.info(f'O.K got objects from database:{obj} HTTP/1.1 200 OK')
    return obj

# generates info log for successful response 
def ok_status_200(obj, obj_name):
    logger.info(f'O.K for {obj_name} : {obj}  HTTP/1.1 200 OK')
    return obj

# generates info log when check error is false
def ok_chek_error_is_false(model):
    logger.info(f'O.K check error at {model} is FALSE. status HTTP/1.1 200 OK')

# generates info log for successful instance creating
def ok_status_201(obj, model):
    logger.info(f'O.K new instance BEEN CREATED: {obj} at model {model} - HTTP/1.1 201 OK')
    return obj

# generates success info log and jsonresponse
def ok_status_201_json(obj, model):
    logger.info(f'O.K new instance BEEN CREATED: {obj} at model {model} - HTTP/1.1 201 OK')
    msg = JsonResponse({'status':'success', 'Datails':str(obj) }, status=201, safe=False)
    return msg

# generates info log when data is successfully serialized
def ok_got_serialzed_data(serialized_data):
    logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1 200 OK')

# generates info log when serialized data is valid
def serialzed_data_is_valid():
    logger.info(f'O.K serialized data IS VALID HTTP/1.1 200 OK')

# generates success info log and jsonresponse
def success_jsonResponse(obj):
    logger.info('O.K returning success_jsonResponse HTTP/1.1 200 OK')
    msg = JsonResponse({'status': 'success O.K HTTP/1.1 200', 'Details': obj}, status=200, safe=False)
    return msg

# generates info log when validating data successfully
def ok_vlidate_data(model, func):
    logger.info(f'OK GOT VALIDATE data at model:{model} - func:{func}  HTTP/1.1 200 OK')

# generates info log when validating object successfully
def ok_vlidate_obj(obj):
    logger.info(f'OK GOT VALIDATE obj:{obj}   HTTP/1.1 200 OK')

# generates success info log and jsonresponse when authentication is successful
def ok_auth(user):
    logger.info(f'Authentication successful: {user} HTTP/1.1 200 OK')
    username = user['name']
    role = user['role']
    id = user['id']
    response_data = {
        'message': 'Authentication successful.',
        'name': username,
        'role': role,
        'id' : id
    }

    return JsonResponse(response_data)

# generates success info log and jsonresponse when logging out is successful
def ok_logout():
    logger.info('O.K logged out HTTP/1.1 200 OK')
    msg = JsonResponse({'status':'logged out'})
    return msg

# generates info log when session state is active
def session_is_active(state):
    logger.info(f'session is {state} active')

# generates success info log and jsonresponse
def status_200_json(object, obj_name):
        logger.info(f'O.K got object/list HTTP/1.1" 200')
        return JsonResponse({obj_name: object}, status=200)

# generates info log with mthod type when a request is received
def got_request(request):
    msg =logger.info(f'{request.method} request received HTTP/1.1" 100')
    return msg

# generates info log when serialized data is valid 
def got_serialized_valid_data():
    logger.info(f'O.K got user valid data - HTTP/1.1" 200')

# generates success info log and jsonresponse for a successful object delete
def ok_status_204(object_id):
    logger.info(f'O.K object no.{object_id} been deleted - HTTP/1.1 204 No Content')
    msg = JsonResponse({'status':'success', 'Datails':f'O.K object no.{object_id} been deleted - HTTP/1.1 204 No Content' }, status=201, safe=False)
    return msg


