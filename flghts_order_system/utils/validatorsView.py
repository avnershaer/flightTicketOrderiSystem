import re
import os
from loggers import *
from django.http import JsonResponse
from PIL import Image
from .response_messages import *
from django.utils import timezone
from ..dal.models import Flights, Tickets

'''
GetValidations class is a utility class designed to provide validation methods,
for various types of data, such as names, email addresses, passwords, and numbers. 

'''


errlogger = errLogger()
logger = lggr()


class GetValidations():
    
    # vildating name
    def validate_name(self, request, obj):
        ok_move_to(model='ValidatorsView.GetValidations', func='validate_name()')
        
        name = request.data.get(obj)
        logger.info(f'name: {name}')
        try:
            # regex pattern for validating name string format onley letters a-z A-Z , 1 space alowwed,  3-30 charts 
            pattern = r'^(?!.*\s.*\s)[A-Za-z0-9\s]{3,30}$'
            
            # check if name matches the pattern
            if not re.match(pattern, name):
                errlogger.error(f'Invalid data format   HTTP/1.1 400 Bad Request')
                logger.info(f'no mach for {name}')
                # if no match, return error response
                return JsonResponse({'error':f"Invalid data format for {name}: data must be onley letters a-z A-Z , 1 space alowwed, with a minimum length of 3 characters and maximum of 30."}, status=400)
            
            logger.info(f'data:{name} been validated returning "True" - HTTP/1.1 200 OK')
            
            # if match, return True, indicating successful validation
            return True
        
        # handle any exceptions that occur during validation
        except Exception as e:
            return error_500(e=e, model='GetValidations.validate_name()')
        
    # vildating username
    def validate_user_name(self, request, obj):
            ok_move_to(model='ValidatorsView.GetValidations', func='validate_user_name()')
            
            username = request.data.get(obj)
            try:
                # regex pattern for validating username string format  A-Z a-z 0-9 _ - min 3 ltters no spaces allowd
                pattern = r'^[A-Za-z0-9_-]{3,}$'
                
                # check if username matches the pattern
                if not re.match(pattern, username):
                    errlogger.error('Invalid data format  HTTP/1.1 400 Bad Request')
                    
                    # if no match, return error response
                    return JsonResponse({'error':f"Invalid data format for {username}: data must be onley A-Z a-z 0-9 _ - and <3 ltters - no spaces allowd"}, status=400)
                
                logger.info(f'data:{username} been validated returning "True" - HTTP/1.1 200 OK')
                
                # if match, return True, indicating successful validation
                return True
            
            # handle any exceptions that occur during validation
            except Exception as e:
                return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.validate_user_name()')
        
    # vildating email
    def validate_email(self, request, obj):
        ok_move_to(model='ValidatorsView.GetValidations', func='validate_email()')
        
        email = request.data.get(obj)
        try:
            # regex pattern for validating email string format - "user@example.com"
            pattern = r'^(?=.{1,254}$)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
            
            # check if email matches the pattern
            if not re.match(pattern, email):
                errlogger.error('Invalid email format: The email address must be in the format "user@example.com"')
                
                # if no match, return error response
                return JsonResponse({'error':f"Invalid email format {email}: must be in the format 'user@example.com', 2-250 charters, [A-Za-z0-9 . _ % + -]"}, status=400)
            
            logger.info(f'email:{email} been validated returning "True" - HTTP/1.1 200 OK')
            
            # if match, return True, indicating successful validation
            return True
        
        # handle any exceptions that occur during validation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.validate_email()')
    
    # vildating password
    def validate_password(self, request, obj):
        ok_move_to(model='ValidatorsView.GetValidations', func='validate_password()')
        
        # get password from request
        password = request.data.get(obj)
        
        logger.info(f'request.data.get(password): {password}')
        try:
            # regex pattern for validating password string format, one digit, one lowercase letter, min 6 charts
            pattern = r'^(?=.*\d)(?=.*[a-z]).{6,}$'
            
            # check if password matches the pattern
            if not re.match(pattern, password):
                errlogger.error('Invalid data format  HTTP/1.1 400 Bad Request')
                
                # if no match, return error response
                return JsonResponse({'error':f"Invalid password format {password}: password must contain at least one digit, one lowercase letter, and must be at least 6 characters long"}, status=400)            
            
            logger.info(f'password:{password} been validated returning "True" - HTTP/1.1 200 OK')
            
            # if match, return True, indicating successful validation
            return True
        
        # handle any exceptions that occur during validation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.validate_password()')
    
    
    # simple regex number validation, for received phone numbers and credit cards numbers
    def validate_phone_number(self, request, obj): 
        ok_move_to(model='ValidatorsView.GetValidations', func='validate_number()')

        try:
            number = request.data.get(obj)
            # regex pattern for validating numbers only, up to 20 digits, no spaces allowed
            pattern = r'^\d{3}-\d{7}$'
            
            # check if number matches the pattern
            if not re.match(pattern, number):
                errlogger.error('Invalid data format  HTTP/1.1 400 Bad Request')
                
                # if no match, return error response
                return JsonResponse({'error':f'Invalid data format for {number}: data must be at this pattern: "123-4567890"'}, status=400)            
            
            logger.info(f'data:{number} been validated returning "True" - HTTP/1.1 200 OK')
            
            # if match, return True, indicating successful validation
            return True
        
        # handle any exceptions that occur during validation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.validate_password()')

# simple regex number validation, for received phone numbers and credit cards numbers
    def validate_creditcard_number(self, request, obj): # simple regex number validation, for received phone numbers and credit cards numbers
        ok_move_to(model='ValidatorsView.GetValidations', func='validate_number()')

        number = request.data.get(obj)
        try:
            # regex pattern for validating numbers only, up to 20 digits, no spaces allowed
            pattern = r'^\d{13,19}$'
            
            # check if number matches the pattern
            if not re.match(pattern, number):
                errlogger.error('Invalid data format  HTTP/1.1 400 Bad Request')
                
                # if no match, return error response
                return JsonResponse({'error':f'Invalid data format for {number}: data must be onley 13 to 19 digits. no spaces allowed'}, status=400)            
            
            logger.info(f'data:{number} been validated returning "True" - HTTP/1.1 200 OK')
            
            # if match, return True, indicating successful validation
            return True
        
        # handle any exceptions that occur during validation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.validate_password()')

    # validates an uploaded image file
    def validate_pic_image(self, pic_imge):
        ok_move_to(model='ValidatorsView.GetValidations', func='validate_pic_image()')
        
        try:
            # open the provided image using PIL
            image = Image.open(pic_imge)
        except Exception as e:
            return error_500(e=e, model='GetValidations.validate_pic_image()')
        
        try:
            # list of allowed image types
            allowed_types = ['image/jpeg', 'image/png', 'image/gif']

            # maximum file size in bytes (2MB)
            max_size = 2 * 1024 * 1024  
            max_width = 1000
            max_height = 1000

            # get the size of the image
            image_width, image_height = image.size
            logger.info(f'got image size: {image.size} ')

            # allowed characters in the file name (A-Z, a-z, 0-9, _, -, and .)
            allowed_characters = r'^[A-Za-z0-9_.-]+$'

            # extract the file name from the provided image
            file_name = os.path.basename(pic_imge.name)
            logger.info(f'got file name: {file_name} ')

            # check if the content type of the image is in allowed types list
            if pic_imge.content_type not in allowed_types:

                # not allowed, return error respone 
                errlogger.error(f'the content type of the image: {pic_imge.content_type},  is in allowed types list')
                return error_500(e='Invalid file type. Allowed types: JPEG, PNG, GIF.', model='')

            # check if the file size is within the maximum limit
            if pic_imge.size > max_size:

                # file size is not within the maximum limit, return error respone 
                errlogger.error(f'the file size: {pic_imge.size}, is not within the maximum limit')
                return error_500(e='File size exceeds the maximum limit (2MB).', model='')

            # check if image size is within the maximum limits
            if image_width > max_width or image_height > max_height:

                # image size is not within the maximum limit, return error respone 
                errlogger.error(f'the image size is not within the maximum limit')
                return error_500(e='Image size is too big - maximum limit 1000x1000.', model='')

            # check if the file name contains only allowed characters
            if not re.match(allowed_characters, file_name):

                # file name contains not allowed characters, return error respone 
                errlogger.error(f'invalid file name: {file_name}')
                return error_500(e='Invalid file name. onley A-z a-z, 0-9, - , _ , and . are allowed.', model='')

            # image file validated, returns the image
            return pic_imge
    
        # handle any exceptions that occur during validation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.validate_pic_image()')

    # check if the object is JsonResponse
    def if_isinstance(self, obj):
        ok_move_to(model='ValidatorsView.GetValidations', func='if_isinstance()')
        try:
            # check if the object is an instance of JsonResponse
            if isinstance(obj, JsonResponse):
                errlogger.error('got error at validatorsfuncs.if_isinstance')

                # is JsonResponse, return the error object
                return obj 

            # return False indicate no error
            logger.info('OK got no errors at validatorsfuncs.if_isinstance, returning False')   
            return False

        # handle any exceptions occurs during func operation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.if_isinstance()')
    
    
    # valid the amount of the remaining tickects
    def valid_remaining_tickects(self, amount_of_tickets):
        ok_move_to(model='ValidatorsView.GetValidations', func='valid_remaining_tickects()')
        logger.info(f'amount_of_tickets:{amount_of_tickets}')  
        try:
            if int(amount_of_tickets) < 1:

                # amount_of_tickets < 1 returns error response
                errlogger.error(f'ERROR: amount_of_tickets < 1 **{amount_of_tickets}**  HTTP/1.1 500')
                return JsonResponse({'ERROR':'** HTTP/1.1 500', 'details':f'amount_of_tickets < 1 **{amount_of_tickets}** HTTP/1.1 500'}, status=500)

            # number of tickets is greater than 0 return True indicate no error
            logger.info(f'OK amount_of_tickets > 0   HTTP/1.1 200')
            return True
        
        # handle any exceptions occurs during func operation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.valid_remaining_tickects()')
    
    # valid departure time is not in the past
    def valid_departure_time(self, dep_time):
        ok_move_to(model='ValidatorsView.GetValidations', func='valid_departure_time()')
        
        try:
            # get the current time
            time_now = timezone.now()

            # check if departure time is before current time
            if dep_time < time_now:

                # departure time is before current time, returns error response
                errlogger.error(f'ERROR: can not update or create flight for a past date :{dep_time} - HTTP/1.1 500 ')
                return JsonResponse({'status':'ERROR', 'details':f'can not update or create flight for a past date:{dep_time} - HTTP/1.1 500'}, status=500)

            # departure time is not before current time, return True indicate no error
            logger.info('departure time is OK - HTTP/1.1 200')
            return True

        # handle any exceptions occurs during func operation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.valid_departure_time()')
    
    
    # valid landing time is not before the departure time
    def valid_landing_time(self, land_time, dep_time):
        ok_move_to(model='ValidatorsView.GetValidations', func='valid_landing_time()')
        
        try:
            # chek if landing time not before the departure time
            if land_time < dep_time:

                # landing time is before the departure time, returns error response
                errlogger.error(f'ERROR: can not update or create flight for a flight whith landing time({land_time}) before departure time({dep_time})  - HTTP/1.1 500 ')
                return JsonResponse({'status':'ERROR', 'details':f'can not update or create flight for a flight whith landing time({land_time}) before departure time({dep_time}) - HTTP/1.1 500'}, status=500)

            # landing time is not before the departure time, return True indicate no error    
            logger.info('landing time is OK - HTTP/1.1 200')
            return True
        
        # handle any exceptions occurs during func operation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.valid_departure_time()')
    
    # valid that origin and destination countries are not the same
    def valid_origin_destination_country(self, origin_country_id, destination_country_id):
        ok_move_to(model='ValidatorsView.GetValidations', func='valid_origin_destination_country()')
        
        try:
            # check origin and destination countries are not the same
            if int(origin_country_id) == int(destination_country_id):

                # origin and destination countries are the same, returns error response
                errlogger.error(f'ERROR: origin_country_id = destination_country_id - cannot add internal flight - HTTP/1.1 500')
                return JsonResponse({'details': 'ERROR origin_country_id = destination_country_id - cannot add internal flight - HTTP/1.1 500'}, status=500)

            # origin and destination countries are not the same, return True indicate no error
            logger.info('OK origin_country_id != destination_country_id - HTTP/1.1 200')
            return True
        
        # handle any exceptions occurs during func operation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.valid_origin_destination_country()')
    
    # valid if user authenticated for adding or updating object
    def valid_user_for_add_update(self, request, air_line_id):
        ok_move_to(model='ValidatorsView.GetValidations', func='valid_user_for_add_update()')
        
        try:
            # import necessary module to prevent circular import
            from .operation_funcs import get_airline_id_by_user_id   
            
            # get the airline_id from the session using the provided request
            airline_id = get_airline_id_by_user_id(request)
            
            # check if the instance is not JsonResponse(indicating error)
            if not self.if_isinstance(airline_id):
                
                # not JsonResponse
                ok_chek_error_is_false(model=f'---{airline_id}  {air_line_id} ---Validators.valid_user_for_add_update()')
                
                # check if the user's airline_id matches the provided air_line_id
                if air_line_id == airline_id:
                    
                
                    # air_line_id = airline_id, user is authorized to continue adding or updating, returns True indicate no error
                    logger.info('OK - user_id mach entity_id - user authorize continue adding or updating')
                    return True
                
                # air_line_id != airline_id, user is not authorized to continue adding or updating, returns error response
                errlogger.error(f'airline_id: {airline_id} dont match air_line_id {air_line_id}')
                return error_403(e=f'airline_id: {airline_id} dont match air_line_id {air_line_id}')
            
            # if user_id is not found returns error response
            return error_404(e='ERROR: "user_id" NOT FOUND', obj='valid_user_for_add_update', model='valodatorsViews')
        
        # handle any exceptions occurs during func operation
        except Exception as e:
            return error_500(e=f'ERROR: got wrong data **{e}', model='GetValidations.valid_origin_destination_country()')
        
    def check_enough_tickets(self, flight_id):
        ok_move_to(model='ValidatorsView.GetValidations', func='check_enough_tickets()')
        try:
           
            # get the flight instance and the remaining_tickets value 
            flight = Flights.objects.get(flight_id=flight_id)
            remaining_tickets = flight.remaining_tickects
           
            # checks if the amount of tickets is less then 1
            if remaining_tickets < 1:          
                # return error if there is less then 1 ticket
                return error_500(e=f'not enough tickets *{remaining_tickets}* HTTP/1.1 500', model='ValidatorsView.GetValidations.valid_amount_of_tickects')
            else:
                # if enough tickets:
                logger.info(f'OK got enough tickets *{remaining_tickets}* - returning TRUE HTTP/1.1 200')
                #return True
       
        except Exception as e:
            return error_500(e=e, model='ValidatorsView.GetValidations.check_enough_tickets()')

    def valid_auth_for_delete(self, request, entity_id, model, entity):
        from .operation_funcs import get_user_id_from_token, get_airline_id_by_user_id
        from ..dal.dalViews import Dal
        
        user_id = get_user_id_from_token(request=request)
        logger.info(f'OK got user_id {user_id}')
        
        air_line_id = get_airline_id_by_user_id(request)
        logger.info(f'OK got air_line_id {air_line_id}')
        
        instance = Dal().get_object_by_entity_id(id=entity_id, model=model, entity=entity)
        logger.info(f'OK got instance {instance.air_line_id}')
        
        if instance.air_line_id.air_line_id != air_line_id:
           return error_403(e='for deleting this object') 
        logger.info(f'OK AUTHORIZED for deleting HTTP/1.1  403 - instance.air_line_id ({instance.air_line_id}:{instance.air_line_id.air_line_id}) == air_line_id {air_line_id}')
        return True 
        
    def valid_user_for_operation(self, request, model, model1, attr_name, id, attr_name2, operation):
        ok_move_to(model='validatorsView', func=f'valid_auth_for_operation()')
        try:
            # import necessary module to prevent circular import

            from .operation_funcs import  get_object_id_by_user_id
            from ..dal.dalViews import Dal

            # get object id using session token 
            object_id = get_object_id_by_user_id(request=request, instance=model, entity_id=attr_name2)
            logger.info(f'OK got object_id **{object_id}**')

            # get the instance using the entity_id(id)
            instance = Dal().get_object_by_entity_id(id=id, model=model1, entity=attr_name)
            if not self.if_isinstance(instance):
                
                # get the attribute name using getattr func
                instance_attr_id = getattr(instance, attr_name2)
                if isinstance(instance_attr_id, int):
                    logger.info(f'OK got attribute ID **{instance_attr_id}**')
                    instance_attr_value = instance_attr_id
                else:    
                    logger.info(f'OK got attribute NAME **{instance_attr_id}**')
                   
                   
                    instance_attr_value = getattr(instance_attr_id, attr_name2)  # get the value of object_id
                    logger.info(f'OK got instance {attr_name} **{instance_attr_value}**')
                if instance_attr_value == object_id:
                    logger.info(f'OK AUTHORIZED for **{operation} --instance_attr_id {instance_attr_id}--instance_attr_value{instance_attr_value}--object_id{object_id}**  - HTTP/1.1  403 ')
                    return True
                else:
                    return error_403(e=f'for {operation} --instance_attr_id *{instance_attr_id}* instance_attr_value *{instance_attr_value} * object_id *{int(object_id)}*') 
            else:
                return instance
        except Exception as e:
            return error_500(e=e, model='validatorsVeiw.valid_user_for_operation()')
    
    # check if customer have more than 2 tickets for current flight
    def check_cust_tickets(self, cust_id, flight_id):
        ok_move_to(model='validatorsView', func='check_cust_tickets')

        try:
            # import necessary module to prevent circular import
            from ..dal.dalViews import Dal

            # get all tickets associated with cust_id
            tickets = Dal().get_object_by_entity_id(id=cust_id, model=Tickets, entity='cust_id')
            ok_got_back(view='Dal().get_object_by_entity_id', obj=tickets)

            # check if the retrieved tickets are in list format, indicate there is more then 1 ticket
            if isinstance(tickets, list):   

                # count the number of tickets with flight_id
                num_tickets_with_flight_id = sum(1 for ticket in tickets if int(ticket.flight_id.flight_id) == int(flight_id))
                logger.info(f'Found *{num_tickets_with_flight_id}* objects with flight_id: *{flight_id}*')

                # check if the number of tickets with flight_id is greater than or equal to 2
                if num_tickets_with_flight_id >= 5:

                    # return False if the customer has 2 or more tickets for the same flight
                    return False

                # return True if the customer has less than 2 tickets for the same flight
                return True

            # return True if there are no tickets associated with the cust_id
            return True
        
        # handle any exceptions occurs during process 
        except Exception as e:
            return error_500(e=e, model='validatorsVeiw.check_cust_tickets()')
        
    # acquiring object data from request and validate it
    def acquire_validate_object(self, request, obj, validator_method):
        ok_move_to(model='operation_funcs', func='acquire_validate_object()')
        try:    
            # validate obj_data
            valid_obj_data = validator_method(request, obj)
            
            # validation fails, return error message
            if valid_obj_data is not True:
                return valid_obj_data

            # successful validation returns the obj_data
            logger.info(f'O.K {obj} IS VALID status OK HTTP/1.1 200')
            return request.data.get(obj)
        
        # handle any exceptions occurs during process 
        except Exception as e:
            return error_500(e=e, model='validatorsVeiw.acquire_validate_object()')

    def check_if_tickets_were_sold(self, flight_id):
        from ..dal.dalViews import Dal
        tickets = Dal.get_object_by_entity_id(id=flight_id, model=Tickets, entity='flight_id')
        if isinstance(tickets, JsonResponse):
            return False
        return True
        