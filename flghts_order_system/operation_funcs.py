from .Serializers import *
from .messages import *
from django.contrib.auth.backends import ModelBackend
from .models import Users
from django.contrib.auth import get_user_model
import json
from functools import wraps
from rest_framework.views import APIView
from .models import Customers, AirLineCompanies

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

def check_session_active(request):
    ok_move_to(model='operation_funcs', func='check_session_active')
    try:
        if request.session.session_key: # Session is active
            session_is_active(state=' -ERROR- ALREADY')
            return True
        else: # Session is not active
            session_is_active(state=' -OK- NOT')
            return False
    except Exception as e: 
        return error_500(e=e, model='check_session_active')

def auth_user(request, user, password):
        ok_move_to(model='operation_funcs', func='auth_user')
        try:    
            request.session['username'] = user['user_name'] 
            request.session.set_expiry(3600)
            session_user_name = request.session.get('username', None)
            logger.info(f'request.session ["username"] = {session_user_name}')
            if user and password == user['password']:
                logger.info('Password is correct')
                login_token = create_token(request, user)
                ok_got_back(view='create_token', obj='login_token')
                return login_token
            else: 
                return auth_failed() # if user_instance is None, authentication failed
        except Exception as e:
            return error_500(e)

def create_token(request, user):
    ok_move_to(model='operation_funcs', func='create_token')
    login_token = LoginToken(id=user['user_id'], name=user['user_name'], role=user['user_role'])
    logger.info(f'roll token created HTTP/1.1 201 OK = {login_token}')
    try:
        request.session['token'] = login_token.to_dict()
        logger.info(f'token added to session HTTP/1.1 200 OK')
        return ok_auth(user=login_token.to_dict())
    except Exception as e:
        return error_500(e)

def check_password(user, password, request ):
    ok_move_to(model='operation_funcs', func='check_password')
    try: 
        if user and password == user['password']:
            logger.info('password is valid - HTTP/1.1 200 OK')
            valid_user = auth_user(request, user, password)
            ok_got_back(view='auth_user', obj='valid_user')
            return valid_user
        else: # If user_instance is None, authentication failed
            logger.info('password is not valid - HTTP/1.1  500')
            return auth_failed()
    except Exception as e:
        logger.info(f'problem whith check password: {e} - HTTP/1.1  500')
        return user

def require_role(a):
    def decorator(func):
        ok_move_to(model='operation_funcs', func='wrapper - require_admin_role')
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            if request.session.get('token') and request.session['token']['role'] == a:
                logger.info('successful authentication - HTTP/1.1 200 OK')
                return func(self, request, *args, **kwargs)
            else:
                return error_403()
        return wrapper
    return decorator

def get_user_id_from_token(request):
    ok_move_to(model='operation_funcs', func='get_user_id_from_token')
    try:
        user_id = request.session['token']['id']# retrieve cust_id from the session           
        if user_id is not None: # check if cust_id is available in the session
            logger.info(f'got id :{user_id} from token - HTTP/1.1 200 OK')
            return user_id
        else:
            errlogger.error(f'got None -user_id is NOT FOUND HTTP/1.1 404')
            return None
    except Exception as e:
            return error_500(e=e, model='operation_funcs')

def get_cust_id_by_user_id(request):
    ok_move_to(model='operation_funcs', func='get_cust_id_by_user_id')
    user_id = get_user_id_from_token(request=request)
    if user_id is not None:
        ok_got_back(view='get_user_id_from_token', obj=f'user_id:{user_id}')
        try:
            customer = Customers.objects.get(user_id=user_id)
            logger.info(f'got customer :{customer} - HTTP/1.1 200 OK')
            cust_id = customer.cust_id
            logger.info(f'got cust_id :{cust_id} - HTTP/1.1 200 OK')
            return cust_id
        except:
            return error_403()
    else:
        return error_403()

def get_airline_id_by_user_id(request):
    ok_move_to(model='operation_funcs', func='get_airline_id_by_user_id')
    user_id = get_user_id_from_token(request=request)
    if user_id is not None:
        ok_got_back(view='get_user_id_from_token', obj=f'user_id:{user_id}')
        try:
            airline = AirLineCompanies.objects.get(user_id=user_id)
            logger.info(f'got airline :{airline} - HTTP/1.1 200 OK')
            airline_id = airline.air_line_id
            logger.info(f'got airline_id :{airline_id} - HTTP/1.1 200 OK')
            return airline_id
        except:
            return error_403()
    else:
        return error_403()
        
















class CustomUserModelBackend(ModelBackend):
    def authenticate(self, **kwarg,):
        User = get_user_model()
        try:
            user = User.objects.get(user_name__iexact=kwarg)
            if user.check_password(kwarg):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None


class LoginToken():

    def __init__(self, id, name, role, token_id = 999) -> None:
        self.id = id
        self.name = name
        self.role = role
        self.token_id = token_id 

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'token_id': self.token_id
        }
    
        
class LoginTokenEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, LoginToken):
            return {
                'id': obj.id,
                'name': obj.name,
                'role': obj.role,
            }
        return super().default(obj)
        








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