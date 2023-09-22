from django.views import View
from loggers import *
from ..utils.response_messages.ok_messages import *
from ..api.Serializers import *
from .models import *
from ..utils.operation_funcs import *
from django.utils import timezone
from datetime import timedelta


logger = lggr()
errlogger = errLogger()


# View class for database access and manipulation
class Dal(View):
    
    model = None # resets the model attr

    # get list of model objects from database 
    def table_objects_list(self, model):
        ok_move_to(model='DAL VIEWS', func='table_objects_list')
        
        try:
            # get the list 
            table_list = model.objects.all()
            
            # success respose with list details
            if table_list:
                return ok_obj_from_db(obj=table_list)
            
            # error response 
            return error_404(e='DATABASE ERROR', obj='NOT FOUND', model='DAL')
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return dal_error(e)




    # create a new instance in the database
    def create_new(self, model, **kwarg):
        ok_move_to(model=f'DAL with kwarg:{kwarg}', func='create_new')

        try:

            # if created model is Tickets, check for tickets availability
            if model == Tickets:
                
                # check for tickets availability
                check_ticket_amount = validator.check_enough_tickets(flight_id=kwarg['flight_id_id'])
                
                if isinstance(check_ticket_amount, JsonResponse):
                    # error response if not enough tickets
                    return check_ticket_amount
            
            # handle password and credit card numbers in kwargs
            if 'password' in kwarg: 
                return password_in_kwargs(kwarg=kwarg, model=model)
            
            # Create a new instance
            instance = model.objects.create(**kwarg)
            
            if instance:
                if model == Tickets:
                    # if created model is tickets, decrease 1 ticket from availabletickets
                    return decrease_ticket(flight_id=kwarg['flight_id_id'], obj=instance)
                
                # check if user_id is on created instance (for registration)
                if hasattr(instance, 'user_id'):
                    logger.info(f'O.K new instance BEEN CREATED with user_id: {instance.user_id} at model {model} - HTTP/1.1 201 OK')
                    return ok_status_201(obj=instance, model=model)
                else:
                    logger.info(f'O.K new instance BEEN CREATED without user_id at model {model} - HTTP/1.1 201 OK')
                    return ok_status_201(obj=instance, model=model)
            
            else:
                # error response if instance did not create
                return error_404(e='DATABASE ERROR', obj=instance, model='DAL')
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return dal_error(e)
        
    # get an object from the database by entity id
    def get_object_by_entity_id(self, id, model ,entity):
        ok_move_to(model='DAL VIEWS', func=f'get_object_by_entity_id')
        
        try:
            # get the object
            obj = model.objects.filter(**{entity: id})
            
            # if no object found, return error response
            if len(obj) == 0: 
                errlogger.error(f'ERROR: NOT FOUNT HTTP/1.1 404 - got None object from database')
                return error_404(e='', obj=entity, model=model, oid=id)
            
            # if only one object found, return object
            if len(obj) == 1: 
                logger.info(f'O.K got one object({obj}) from database HTTP/1.1 200')
                return ok_obj_from_db(obj=obj.first())
            
             # if multiple objects found return list of objects
            logger.info(f'O.K got multiple objects from database HTTP/1.1 200')
            logger.info(f'Found {len(obj)} objects with IDs: {[obj for obj in obj]}')
            return ok_obj_from_db(obj=list(obj))
        
         # handle any exceptions that occur during processing this method
        except Exception as e:
            return dal_error(e)

    # get a flight object by date from database
    def get_flights_by_date(self, model, time_type):
        ok_move_to(model='DAL VIEWS', func='get_flights_by_date')
        
        try:
            # get the object
            flights = model.objects.filter(**time_type) 
            
            if flights:
                # check if object one multi or none for appropriate response
                return check_if_db_instance_one_multi_none(instance=flights)
            
            # failed to fetch list
            return error_404(e='HTTP 404 DATABASE ERROR', obj=flights, model='DAL', oid=time_type)
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return dal_error(e)

    # method for fetching list of flights for next 12 hours 
    def get_next_12_hours_flights(self, model, entity, country_id, country_type):
        ok_move_to(model='DAL VIEWS', func='get_last_12_hours_flights')
        
        try:

            # get the current time and calculate the time 12 hours from now
            now = timezone.now()
            next12hours = now + timedelta(hours=12)
            
            # Query the database for flights within the specified time range and matching country_id
            obj = model.objects.filter(**{entity+'__gte':now, entity + '__lt': next12hours, country_type:country_id}) 
            
            # if any matching flights found
            if obj:

                # success response with the retrieved flights
                logger.info(f'got obj:{obj} from database - HTTP/1.1 200 ')
                return check_if_db_instance_one_multi_none(instance=obj)
            
            # error response if no matching flights were found
            return error_404(e='HTTP 404 DATABASE ERROR', obj=entity, model='DAL', oid=country_id)
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return dal_error(e)
    
    # method for updating an object in database
    def update(self, model, id, **kwargs):
        ok_move_to(model=f'DAL VIEWS {kwargs}', func='update')
        
        try:
            # update object wit given id using provided kwargs
            model.objects.filter(pk=id).update(**kwargs)
            
            # get from database the updated instance
            updated_instance = model.objects.filter(pk=id)
            
            # check if the updated instance was found
            if updated_instance:
                
                # success response with updated instance
                logger.info(f'OK GOT updated instance {updated_instance}')
                return ok_obj_from_db(obj=updated_instance)
            
            
            else:
                # error response if the updated instance was not found
                return error_404(e='HTTP 404 DATABASE ERROR', obj=updated_instance, model='DAL')                
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return dal_error(e)

    # method for deleting an object from database
    def delete(self, model, id):
        ok_move_to(model='DAL View', func='delete')
        
        try:
            # attempt to delete the object with the given id from the model
            deletedObject = model.objects.filter(pk=id).delete()
            
            # check if any objects were deleted successfully
            if deletedObject[0] > 0:

                # successful response with id of deleted object
                return ok_status_204(object_id=id)
            
            else:
                # error response indicating a database issue
                return error_404(e='HTTP 404 DATABASE ERROR', obj=model, model='DAL')
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return dal_error(e)

    # method that retrieve an object by the username from the database (for login)
    def get_object_by_username(self, model, name):
        ok_move_to(model='DAL View', func='get_object_by_username')
        
        try:
            # attempt to retrieve an object from the model using a case-insensitive username match
            obj = model.objects.get(user_name__iexact=name)
            
            # check if the object was found
            if obj:

                # successful response with object
                logger.info(f'O.K got obj from database:{obj} HTTP/1.1" 200')
                return obj
            
            else:
                # error response if no object was found
                return error_404(e='HTTP 404 db error', obj=name, model='DAL', status=404)
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
             return JsonResponse({'error': str(e)}, status=500)

    def get_object_by_user_id(self, model, user_id):
        ok_move_to(model='DAL View', func='get_object_by_user_id')
        
        try:
            logger.info(f'user_id:{user_id}')
            # attempt to retrieve object from model
            obj = model.objects.get(user_id=user_id)
            if obj:   
                # successful response with object
                logger.info(f'O.K got obj from database:{obj} HTTP/1.1" 200')
                return obj
            else:
                # error response if no object was found
                return error_404(e='HTTP 404 db error', obj=f'user_id{user_id}', model='DAL', status=404)
        # handle any exceptions that occur during processing this method
        except Exception as e:
             return JsonResponse({'error': str(e)}, status=500)







    



























































    

    
    
        
    



    