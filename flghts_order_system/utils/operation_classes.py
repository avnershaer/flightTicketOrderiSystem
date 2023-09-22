from loggers import *
from .response_messages import *
from .validatorsView import *
from django.utils import timezone
from datetime import datetime


logger = lggr()
errlogger = errLogger()
validator= GetValidations()

'''


class InstanceData contains various methods to process
a different types of data instances, that received on request 


'''
class InstanceData():

    # process and return dict with login_data received data
    def login_data(self, request):
        ok_move_to(model='InstanceData', func='login_data()')
        
        try:
            # acquiring user_name data from request and validate it
            user_name = validator.acquire_validate_object(request=request, obj=('user_name'), validator_method=validator.validate_user_name)

            # if error (jsonresponse) returns, returning it
            if isinstance(user_name, JsonResponse):
                 return user_name
    
            # acquiring password data from request and validate it
            password = validator.acquire_validate_object(request=request, obj=('password'), validator_method=validator.validate_password)

            # if error (jsonresponse) returns, returning it
            if isinstance(password, JsonResponse):
                 return password
              
            logger.info(f'username = {user_name} password = {password}')
            
            # return dict with the extracted username and password after validation 
            return {'username': user_name, 'password': password}

        # handle any exceptions occurs during process login received data
        except Exception as e:
            return error_500(e=e, model='instancedata.login_data()') 

    # process and return dict with ticket_data received data
    def ticket_data(self, request, cust_id):
        ok_move_to(model='InstanceData', func='ticket_data()')
        
        try:

            # get flight_id from request
            flight_id = request.data.get('flight_id')
            logger.info(f'O.K got flight_id:{flight_id} status HTTP/1.1 200')
            
            # return dict with the extracted flight_id and the received cust_id 
            return {'flight_id_id': flight_id, 'cust_id_id': cust_id}

        # handle any exceptions occurs during process ticket received data
        except Exception as e:
            return error_500(e=e, model='instancedata.ticket_data()') 

    # process and return dict with airline_data received data
    def airline_data(self, request, user_id):
        ok_move_to(model='InstanceData', func='airline_data()')
        
        try:

            # acquiring air_line_name data from request and validate it
            air_line_name = validator.acquire_validate_object(request=request, obj=('air_line_name'), validator_method=validator.validate_user_name)

            # if error (jsonresponse) returns, returning it
            if isinstance(air_line_name, JsonResponse):
                 return air_line_name
                
            # get country_id from the request
            country_id = request.data.get('country_id')
            ok_status_200(obj=country_id, obj_name='country_id')
            
            # get country_id from the request
            user_id = user_id
            
            # return dict with the extracted air_line_name and airline_logo(path) after validation 
            return {'air_line_name': air_line_name, 'country_id_id': country_id, 'user_id_id': user_id}
        
        # handle any exceptions occurs during process airline_data received data
        except Exception as e:
            return error_500(e=e, model='InstanceData.airline_data()')
    
    # process and return dict with flight received data
    def flight_data(self, request, air_line_id):
        ok_move_to(model='operation_classes.InstanceData', func='flight_data()')
        logger.info(f'request.data::{request.data}')
        try:
            
            # get departure time from request as string
            departure_time_str = request.data.get('departure_time')  
            logger.info(f'O.K got departure_time:{departure_time_str} status HTTP/1.1 200')
            
            # parse the ISO 8601 format string into a datetime object
            departure_time = datetime.strptime(departure_time_str, "%Y-%m-%dT%H:%M:%SZ")
            
            # make the departure_time aware of UTC timezone
            departure_time_aware = timezone.make_aware(departure_time, timezone.utc)
            
            # validate departure time
            valid_departure_time = validator.valid_departure_time(dep_time=departure_time_aware)
            
            # if validation fails, return error message
            if valid_departure_time is not True:
                 return valid_departure_time
            
            # get departure time from request as string
            landing_time_str = request.data.get('landing_time')
            logger.info(f'O.K got landing_time:{landing_time_str} status HTTP/1.1 200')
            
            # parse the ISO 8601 format string into a datetime object
            landing_time = datetime.strptime(landing_time_str, "%Y-%m-%dT%H:%M:%SZ")
            
            # make the landing_time aware of UTC timezone
            landing_time_aware = timezone.make_aware(landing_time, timezone.utc)
            
            # validate landing_time 
            valid_landing_time = validator.valid_landing_time(land_time=landing_time_aware, dep_time=departure_time_aware)
            
            # if validation fails, return error message
            if valid_landing_time is not True:
                 return valid_landing_time            
            
            # get the remaining tickects account from request remaining_tickects
            remaining_tickets = request.data.get('remaining_tickets')
            logger.info(f'O.K got *-{remaining_tickets}-* remaining tickets: status HTTP/1.1 200')
            
            # validate remaining_tickects > 0
            valid_remaining_tickects = validator.valid_remaining_tickects(amount_of_tickets=remaining_tickets)
            
            # if validation fails, return error message
            if valid_remaining_tickects is not True:
                return valid_remaining_tickects
            
            # get origin_country_id from request
            origin_country_id = request.data.get('origin_country_id')
            logger.info(f'O.K got origin_country_id:{origin_country_id} status HTTP/1.1 200')
            
            # get destination_country_id from request
            destination_country_id = request.data.get('destination_country_id')
            logger.info(f'O.K got destination_country_id:{destination_country_id} status HTTP/1.1 200')
            
            # validate that the origin_country is not same like destination_country
            valid_origin_destination_country = validator.valid_origin_destination_country(origin_country_id=origin_country_id, destination_country_id=destination_country_id)
            
            # if validation fails, return error message
            if valid_origin_destination_country is not True:
                 return valid_origin_destination_country
            
            # return dict with the extracted and validated data
            return {'departure_time': departure_time, 'landing_time': landing_time, 'remaining_tickects':remaining_tickets, 'air_line_id_id':air_line_id, 'origin_country_id_id':origin_country_id, 'destination_country_id_id':destination_country_id}
        
        # handle any exceptions occurs during process login received data
        except Exception as e:
            return error_500(e=e, model='InstanceData.flight_data()')
    
    # process and return dict with new_user received data
    def new_user_data(self, request, user_role):
        ok_move_to(model='operation_classes.InstanceData', func='new_user_data')

        try:
            # acquiring user_name data from request and validate it
            user_name = validator.acquire_validate_object(request=request, obj=('user_name'), validator_method=validator.validate_user_name)

            # if error (jsonresponse) returns, returning it
            if isinstance(user_name, JsonResponse):
                 return user_name
    
            # acquiring password data from request and validate it
            password = validator.acquire_validate_object(request=request, obj=('password'), validator_method=validator.validate_password)

            # if error (jsonresponse) returns, returning it
            if isinstance(password, JsonResponse):
                 return password

            # acquiring password data from request and validate it
            email = validator.acquire_validate_object(request=request, obj=('email'), validator_method=validator.validate_email)

            # if error (jsonresponse) returns, returning it
            if isinstance(email, JsonResponse):
                 return email

            user_role = user_role
            # check if user role is in user roles list
            if user_role in [1, 2, 3]:

                # user role is in user roles list
                logger.info(f'O.K got user_role no.{user_role} status HTTP/1.1 200')

                # return dict with the extracted and validated data
                return {'user_name': user_name, 'password':password, 'email':email, 'user_role_id':user_role, }

            # return error response if user role is not exists
            return error_500(e=f'ERROR - The provided user_role {user_role} is not valid. It must be 1, 2, or 3', model='InstanceData.new_user_data')

        # handle any exceptions occurs during process new_user received data
        except Exception as e:
            return error_500(e=e, model='InstanceData.new_user_data()')
    
    
    # process and return dict with customer received data
    def customer_data(self, request, user_id):
        ok_move_to(model='InstanceData', func='customer_data()')
        try:
            # acquiring cust_first_name data from request and validate it
            cust_first_name = validator.acquire_validate_object(request=request, obj=('cust_first_name'), validator_method=validator.validate_name)
            logger.info(f'cust_first_name: {cust_first_name}')
            # if error (jsonresponse) returns, returning it
            if isinstance(cust_first_name, JsonResponse):
                logger.info(f'cust_first_name:{cust_first_name}')
                return cust_first_name
            
            # acquiring cust_last_name data from request and validate it
            cust_last_name = validator.acquire_validate_object(request=request, obj=('cust_last_name'), validator_method=validator.validate_name)
        
            # if error (jsonresponse) returns, returning it
            if isinstance(cust_last_name, JsonResponse):
                return cust_last_name

            # acquiring cust_adress data from request and validate it
            cust_adress = validator.acquire_validate_object(request=request, obj=('cust_adress'), validator_method=validator.validate_name)   
                
            # if error (jsonresponse) returns, returning it
            if isinstance(cust_last_name, JsonResponse):
                return cust_adress    
            
            # acquiring cust_phone_num data from request and validate it
            cust_phone_num = request.data.get('cust_phone_num')#validator.acquire_validate_object(request=request, obj=('cust_phone_num'), validator_method=validator.validate_phone_number)   
                
            cust_credit_card_num = request.data.get('cust_credit_card_num')
            # return dict with the extracted and validated data
            return {'cust_first_name': cust_first_name, 'cust_last_name': cust_last_name, 'cust_adress': cust_adress, 'cust_phone_num': cust_phone_num,  'user_id_id': user_id, 'cust_credit_card_num':cust_credit_card_num}
        
        # handle any exceptions occurs during process customer received data
        except Exception as e:
            return error_500(e=e, model='InstanceData.customer_data()')
        
    # process and return dict with administrator received data
    def administrator_data(self, request, user_id):
        ok_move_to(model='InstanceData', func='administrator_data()')
        try:
            # acquiring admin_first_name data from request and validate it
            admin_first_name = validator.acquire_validate_object(request=request, obj=('admin_first_name'), validator_method=validator.validate_user_name)

            # if error (jsonresponse) returns, returning it
            if isinstance(admin_first_name, JsonResponse):
                 return admin_first_name
             
            
            # acquiring admin_last_name data from request and validate it
            admin_last_name = validator.acquire_validate_object(request=request, obj=('admin_last_name'), validator_method=validator.validate_user_name)

            # if error (jsonresponse) returns, returning it
            if isinstance(admin_last_name, JsonResponse):
                 return admin_last_name
    
            # return dict with the extracted and validated data
            return {'admin_first_name': admin_first_name, 'admin_last_name': admin_last_name, 'user_id_id': user_id}
        
        # handle any exceptions occurs during process new_user received data
        except Exception as e:
                        return error_500(e=e, model='InstanceData.administrator_data()')