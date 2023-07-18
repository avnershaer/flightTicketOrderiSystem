from django.views import View
from ..loggers import *
from ..messages import *
from ..Serializers import *
from ..models import *

logger = lggr()
errlogger = errLogger()

class Dal(View):

    model = None

    def table_objects_list(self, model):
        ok_move_to(model='DAL VIEWS')
        try:
            table_list = model.objects.all()
            if table_list:
                return ok_obj_from_db(object=table_list)
            else:
                return error_404(
                    e='HTTP 404 DATABASE ERROR', 
                    obj='NOT FOUND', model='DAL'
                    )
        except Exception as e:
            return JsonResponse({'DAL ERROR': str(e)})

    def get_object_by_entity_id(self, id, model ,entity):
        ok_move_to(model='DAL VIEWS')
        try:
            obj = model.objects.filter(**{entity:id})
            if obj:
                return ok_obj_from_db(object=obj)
            else:
                return error_404(
                    e='HTTP 404 DATABASE ERROR', 
                    obj=entity, model='DAL'
                    )
        except Exception as e:
             return JsonResponse({'DAL ERROR': str(e)})

    def get_flights_by_date(self, date, model):
        ok_move_to(model='DAL VIEWS')
        try:
            flights = model.objects.filter(departure_time__date = date)
            if flights:
                return ok_obj_from_db(object=flights)
            else:
                return error_404(
                    e='HTTP 404 DATABASE ERROR', 
                    obj=flights, model='DAL'
                    )
        except Exception as e:
             return JsonResponse({'DAL ERROR': str(e)})

    def get_last_12_hours_flights(
            self, 
            last12hours, 
            model, 
            entity, 
            country_id, country_type
            ):
        ok_move_to(model='DAL VIEWS')
        try:
            obj = model.objects.filter(
                **{
                entity + '__lte': last12hours, 
                country_type: country_id
                }
                ) 
            if obj:
                return ok_obj_from_db(object=obj)
            else:
                return error_404(
                    e='HTTP 404 DATABASE ERROR', 
                    obj=entity, model='DAL'
                    )
        except Exception as e:
             return JsonResponse({'DAL ERROR': str(e)})


    def create_new(self, model, **kwarg):
        ok_move_to(model='DAL VIEWS')
        try:
            logger.info(f'OK GOT SERIALZE 3 VALID DATA dalVIEW {kwarg}')
            instance = model.objects.create(**kwarg)
            if instance: 
                logger.info(f'OK GOT SERIALZE 4 serializers.serialize {instance}')
                return instance
            else:
                return error_404(
                    e='HTTP 404 DATABASE ERROR', 
                    obj=instance, 
                    model='DAL'
                    )
        except Exception as e:
            return JsonResponse({'DAL ERROR': str(e)})
        
    def Update(self, model, id, **kwargs):
        ok_move_to(model=f'DAL VIEWS {kwargs}')
        try:
            model.objects.filter(pk=id).update(**kwargs)
            updated_instance = model.objects.filter(pk=id)
            if updated_instance:
                logger.info(f'OK GOT updated instance {updated_instance}')
                return ok_obj_from_db(object=updated_instance)
            else:
                return error_404(
                    e='HTTP 404 DATABASE ERROR', 
                    obj=updated_instance, 
                    model='DAL'
                    )                
        except Exception as e:
            return JsonResponse({'DAL ERROR': str(e)})


    def delete(self, model, id):
        ok_move_to(model='DAL View')
        try:
            deletedObject = model.objects.filter(pk=id).delete()
            if deletedObject[0] > 0:
                return ok_status_204(object_id=id)
            else:
                return error_404(
                    e='HTTP 404 DATABASE ERROR', 
                    obj=model, 
                    model='DAL'
                    )
        except Exception as e:
            return JsonResponse({'DAL ERROR': str(e)})



























































    

    
    
        
    def getById(self, model, id):
        try:
            obj = model.objects.get(pk=id)
            return obj
        except Exception as e:
            errlogger.error()
            return {'DAL error': str(e)}
        
    
        
    def get_object_by_username(self, model, name):
        try:
            obj = model.objects.select_related('user_id').get(user_id__user_name__iexact=name)
            if obj:
                logger.info(f'O.K got obj from database:{obj} HTTP/1.1" 200')
                return obj
            else:
                return error_404(e='HTTP 404 db error', obj=name, model='DAL')
        except Exception as e:
             return JsonResponse({'DAL ERROR': str(e)})

    
    


def get_customer_by_username(self, username, model, users):
        try:
            user = users.objects.filter(user_name__iexact=username).first()
            if user:
                customer = model.objects.filter(user_id=user).first()
                if customer:
                    return customer
            return None
        except Exception as e:
            # Handle the exception or return an error response
            return None

  
    
    
    #def arrival_flights(self, id):
    #        try:
    #            obj = Flights.objects.filter(origin_country_id=id)
    #            if obj:
    #                logger.info(f'O.K. Got object from database: {obj} HTTP/1.1" 200')
    #                return obj
    #            else:
    #                msg =f'DAL ERROR: cannot get object:{obj} from db'
    #                errlogger.error(msg)
    #                return msg
    #        except Exception as e:
    #             return {'DAL ERROR': str(e)}
















    