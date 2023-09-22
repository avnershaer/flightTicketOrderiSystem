from ..api.Serializers import *
from .response_messages import *
#from django.contrib.auth.backends import ModelBackend
#from ..dal.models import Users
#from django.contrib.auth import get_user_model
import json
from functools import wraps
#from rest_framework.views import APIView
from ..dal.models import Customers, AirLineCompanies, Flights #Tickets
from .operation_classes import InstanceData
from django.contrib.auth.hashers import make_password, check_password



instance_data= InstanceData()

# serializes data 
def serialize_data(instance_model, model_serializer, objects, many):
    ok_move_to(model='operation_funcs', func='serialize_data')
    
    try:
        # if there are objects to serialize
        if objects:
            logger.info(f'O.K GOT objects HTTP/1.1 200 {instance_model}')
            
            # serialize the objects using the provided model serializer
            serializer = model_serializer(objects, many=many)
            logger.info(f'O.K  objects BEEN SERIALIZED HTTP/1.1 200')
            
            # successful jsonresponse with serialized data
            return success_jsonResponse(obj=serializer.data)
        
        # if no objects to serialize
        else:
            # error jsonresponse if serialized data is not valid
            return serialzed_data_NOT_valid(obj=objects)
    
    # handle any exceptions that occur during processing this method
    except Exception as e:
        return error_500(e, model='operation_funcs.serialize_data()')
 

# checks if got one multi or none object
def check_one_multi_none(obj, instance_model, model_serializer):
    ok_move_to(model='operation_funcs', func=f'check_one_multi_none--------------{obj}')
    
    try:
        # if there is no objects
        if obj == None:

            # error 404 response
            return error_404(e='', obj=obj, model=instance_model, oid='') 
            
        #if there is one object
        elif isinstance(obj, instance_model): 
            logger.info(f'O.K got one object from database HTTP/1.1 200')
            
            # serialize the single object
            sobj = serialize_data(model_serializer=model_serializer, instance_model=instance_model, objects=obj, many=False)
            
            # returns the serialized object
            return sobj
        
        # if there is multiple objects (list with len of 2 objects and more)
        elif len(obj) > 1: 
            logger.info(f'O.K got multiple objects from database HTTP/1.1 200')
            
            # serialize multiple objects
            sobj = serialize_data(model_serializer=model_serializer, instance_model=instance_model, objects=obj, many=True)
            
            # returns the serialized objects
            return sobj
   
    # handle any exceptions that occur during processing this method
    except Exception as e:
        return error_500(e=e, model='operation_funcs.check_one_multi_none()')

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

# checks if the session is active in request
def check_session_active(request):
    ok_move_to(model='operation_funcs', func='check_session_active')
    
    try:
        #  if the session key exists in request
        if request.session.session_key: 
            session_is_active(state=' -ERROR- ALREADY')
            return True
        
        # if session key doesn't exist in request
        session_is_active(state=' -OK- NOT')
        return False
    
    # handle any exceptions that occur during session check
    except Exception as e: 
        return error_500(e=e, model='operation_funcs.check_session_active()')

# authenticates user using provided request, username, and password
def auth_user(request, user, password):
        ok_move_to(model='operation_funcs', func='auth_user')
        
        try:   
            # set the "username" session key with user's username 
            request.session['username'] = user['user_name'] 
            
            # Set session expiry time to 3600 seconds (1 hour)
            request.session.set_expiry(3600)
            
            # retrieve the session's username
            session_user_name = request.session.get('username', None)
            logger.info(f'request.session ["username"] = {session_user_name}')
            
            # check if the user exists and the password matches (check hashed password)
            if user and check_password(password, user['password']): 
                logger.info('Password is correct')
                
                # creating and returning the login token
                login_token = create_token(request, user)
                return login_token
            
            # if user doesn't exist or password doesn't match, authentication failed
            return auth_failed() 
        
        # handle any exceptions that occur during authentication
        except Exception as e:
            return error_500(e=e, model='operation_funcs.auth_user()')

# create a new LoginToken
def create_token(request, user):
    ok_move_to(model='operation_funcs', func='create_token')
    
    try:
        # create new LoginToken instance using user information
        login_token = LoginToken(id=user['user_id'], name=user['user_name'], role=user['user_role'])
        logger.info(f'roll token created HTTP/1.1 201 OK = {login_token}')

        # add the token as dictionary to the session
        request.session['token'] = login_token.to_dict()
        logger.info(f'token added to session HTTP/1.1 200 OK')
        
        # return success response for authentication, with token's username information
        return ok_auth(user=login_token.to_dict())
    
    # handle any exceptions that occur during token creation
    except Exception as e:
        return error_500(e, model='operation_funcs.create_token()')



## from django.contrib.auth.hashers import make_password, check_password


# check password
def chk_password(request, user, password ):
    ok_move_to(model='operation_funcs', func='chk_password()')
    
    try:
        # authenticate the user and retrieve the valid_user
        valid_user = auth_user(request, user, password)
        ok_got_back(view='auth_user', obj=valid_user)
        
        # return valid_user
        return valid_user
    # handle any exceptions that occur during password checking
    except Exception as e:
        logger.info(f'problem whith check password: {e} - HTTP/1.1  500')
        return user


# define decorator that checks the required roles
def require_role(*roles):
    def decorator(func):
        
        # keep the original function data
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            
            # check if the user is signed in
            if 'token' not in request.session:

                # User is not signed in, return a 403 error
                return error_403('need to sign in')  
            
            # get the user's role from the session
            user_role = request.session.get('token')['role']
            
            # check if the user roles that matches any of the specified roles
            if user_role in roles:
                logger.info('successful authentication - HTTP/1.1 200 OK')
                
                # call the original function with the required role
                return func(self, request, *args, **kwargs)
            
            # error response if the user role doesn't match
            return error_403()
        
        # returning the decorated function
        return wrapper
    
    # return the decorator
    return decorator

# get user_id from session token
def get_user_id_from_token(request):
   
    
    ok_move_to(model='operation_funcs', func='get_user_id_from_token')
  
   
    try:
            user_id = request.session['token']['id']# retrieve cust_id from the session           

            # check if user_id is available on session
            if user_id is not None: 
                logger.info(f'got id :{user_id} from token - HTTP/1.1 200 OK')
                return user_id
            else:
                errlogger.error(f'got None - user_id is NOT FOUND HTTP/1.1 404')
                return None
    
    # handle any exceptions that occur during get user_id from session token
    except Exception as e:
            
            return error_500(e=e, model='operation_funcs.get_user_id_from_token()')

# retrieve the cust_id by the user_id from session token
def get_cust_id_by_user_id(request):
    ok_move_to(model='operation_funcs', func='get_cust_id_by_user_id')
    
    # retrieve user_id from session token using the get_user_id_from_token function
    user_id = get_user_id_from_token(request=request)
    
    # check if user_id available on session
    if user_id is not None:
        ok_got_back(view='get_user_id_from_token', obj=f'user_id:{user_id}')
        
        try:
            # retrieve customer associated with user_id
            customer = Customers.objects.get(user_id=user_id)
            logger.info(f'success retrieveing customer :{customer} - HTTP/1.1 200 OK')
            
            # retrieve cust_id from customer object
            cust_id = customer.cust_id
            logger.info(f'success retrieveing cust_id :{cust_id} - HTTP/1.1 200 OK')
            
            # returns the cust_id
            return cust_id
        
        except:
            # if getting customer fails, return 403 error
            return error_403()
    
    else:
        # if user_id is None, return 403 error
        return error_403()


# retrieve the airline_id by the user_id from session token
def get_airline_id_by_user_id(request):
    ok_move_to(model='operation_funcs', func='get_airline_id_by_user_id')
    
    # retrieve user_id from session token using get_user_id_from_token function
    user_id = get_user_id_from_token(request=request)
    
    # check if user_id available on session
    if user_id is not None:
        ok_got_back(view='get_user_id_from_token', obj=f'user_id:{user_id}')
        
        try:
            # retrieve the airline associated with the user_id
            airline = AirLineCompanies.objects.get(user_id=user_id)
            logger.info(f'success retrieveing airline :{airline} - HTTP/1.1 200 OK')
            
            # retrieve airline_id from airline object
            airline_id = airline.air_line_id
            logger.info(f'success retrieveing airline_id :{airline_id} - HTTP/1.1 200 OK')
            
            # returns the airline_id
            return airline_id
        
        # if getting airline fails, return 403 error
        except:
            return error_403()
    
    # if user_id is None, return 403 error
    else:
        return error_403()
    
# retrieve object_id by the user_id from session token
def get_object_id_by_user_id(request, instance, entity_id):
    ok_move_to(model='operation_funcs', func='get_object_id_by_user_id')
    
    # retrieve user_id from session token using get_user_id_from_token function
    user_id = get_user_id_from_token(request=request)

    # check if user_id available on session
    if user_id is not None:
        ok_got_back(view='get_user_id_from_token', obj=f'user_id:{user_id}')
        
        try:
            # retrieve the object that associated with the user_id
            obj = instance.objects.get(user_id=user_id)
            logger.info(f'got object :{obj} - HTTP/1.1 200 OK')
            
            # using the getattr func to access attribute and get the data
            object_id = getattr(obj, entity_id)  
            logger.info(f'got object_id :{object_id} - HTTP/1.1 200 OK')
            
            # returns the object_id
            return object_id
        
        # if getting airline fails, return 403 error
        except Exception as e:
            return error_403(e=e)
    
    # if user_id is None, return 403 error
    else:
        return error_403()

# delete user 
def user_delete(obj, obj_name, user_id):
    ok_move_to(model='operation_funcs', func='user_delete()')

    # import the necessary module and prevent circular import
    from ..views.facadeViews import FacadeBase

    # deleting user when registration faild
    error_not_created(obj=obj_name)
    FacadeBase().delete_user(user_id=user_id)
    
    # return the provided object
    return obj


def decrease_ticket(flight_id, obj):
    ok_move_to(model='operation_funcs', func='decrease_ticket()')
    logger.info(f'O.K new instance BEEN CREATED at Tickets model - decrease one ticket from flight.remaining_tickects  - HTTP/1.1 201 OK')
    
    try:
        # get the flight using the given flight_id
        flight = Flights.objects.get(flight_id=flight_id)
        
        # get the remaining tickets count
        remaining_tickets = flight.remaining_tickects
        
        # decreasing 1 ticket from remaining tickets count
        flight.remaining_tickects = remaining_tickets - 1
        
        # save the updated flight object with new tickets count
        flight.save()
        logger.info(f'O.K one ticket successfully been decreased from flight.remaining_tickects  - HTTP/1.1 200 OK')
        
        # return the provided object
        return obj

    # handle any exceptions during ticket decreasing
    except Exception as e:
        return error_500(e=e, model='operation_funcs.decrease_ticket()')



def password_in_kwargs(kwarg, model, ):
    ok_move_to(model='operation_funcs', func='password_in_kwargs()')
    logger.info('kwargs contains password')
    
    try:
        # retrieve and remove the raw password from kwargs
        raw_password = kwarg.pop('password')  
        
        # create an instance of the model with the remaining kwargs
        instance = model(**kwarg)
        
        # set the password for the instance (hashing the password)
        instance.set_password(raw_password) 
        ok_got_back(view='instance.set_password', obj=raw_password)
        
        # Check if 'cust_credit_card_num' is in kwargs
        if 'cust_credit_card_num' in kwarg: # check if kwargs contains cust_credit_card_num
            logger.info('kwargs contains cust_credit_card_num')
            
            # retrieve and remove the raw cust_credit_card_num from kwargs
            raw_credit_card = kwarg.pop('cust_credit_card_num')  # remove the cust_credit_card_num from kwargs
            
            # create another instance of the model with the remaining kwargs
            instance = model(**kwarg)
            
            # set the credit card number for the instance (hashing the number)
            instance.set_credit_card(raw_credit_card)  # hash the cust_credit_card_num
    
    # handle exceptions that occur during the process
    except Exception as e:
        return error_500(e=e, model='dal')
    
    # save instance at database
    instance.save()
    logger.info('instance saved')
    
    # indicates that the instance was successfully created with a user_id. 
    if hasattr(instance, 'user_id'):
        logger.info(f'O.K new instance BEEN CREATED with user_id: {instance.user_id} at model {model} - HTTP/1.1 201 OK')
        
        # successful response
        return ok_status_201(obj=instance, model=model)
    
    # return error response if user_id is not found in instance
    return error_404(e='DATABASE ERROR', obj=instance, model='DAL')
                    
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
        