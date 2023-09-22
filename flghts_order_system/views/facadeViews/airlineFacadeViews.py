from .anonimousFacadeViews import AnonymousFacade
from ...api.SysApiViews import *



class AirLinesFacade(AnonymousFacade):

    
    def airline_details_by_user_id(self, request, user_id):
        ok_move_to(model='AirLinesFacade', func='airline_details_by_user_id')
        logger.info(f'request:{request}') 
        try:
             # retrieve the airline associated with the user_id
             airline = api_get_object_by_user_id(model=AirLineCompanies, user_id=user_id, model_serializer=AirlineSerializer)
             ok_got_back(view='api_get_object_by_user_id', obj=airline)
             logger.info(f'success retrieveing airline :{airline} - HTTP/1.1 200 OK')
             
            
             
             # returns the airline_id
             return airline
         
         # if getting airline fails, return 403 error
        except:
             return error_403()
  

    # airline role (2) login require
    @require_role(2)
    # method for getting flights list to logged in airline by token user_id
    def get_my_flights(self, request):
        ok_move_to(model='AirLinesFacade', func='get_my_flights')
        
        try:
            # get airline_id by the user_id from token
            air_line_id = get_airline_id_by_user_id(request=request)
            ok_got_back(view='get_airline_id_by_user_id', obj=f'air_line_id:{air_line_id}')
            
            # check if airline_id was available (False)      
            if validator.if_isinstance(air_line_id) != False: 
                
                # error response
                return air_line_id
            
            try:
                # get list of flights belonging to logged in airline
                my_flights = api_get_object_by_entity_id(id = air_line_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='air_line_id')
                ok_got_back(view='SysApiViews', obj='my_flights')
                
                # success reponse with flights details list or an error response.
                return my_flights
            
            # handle any exceptions that occur during getting flights details list
            except Exception as e:

                # error response
                return air_line_id
            
        # handle any exceptions that occur during processing this method      
        except Exception as e:
            return error_500(e=e, model='airLinesFacadeViews.get_my_flights()')


    # airline role (2) login require
    @require_role(2)
    # method for updating airline details
    def update_airline(self, request, air_line_id):
        ok_move_to(model='AirLinesFacade', func='update_airline')
        
        try:
            # authenticate airline for updating self details
            auth_update = validator.valid_user_for_operation(request=request, model=AirLineCompanies, model1=AirLineCompanies, attr_name='air_line_id', id=air_line_id, attr_name2='air_line_id', operation='UPDATE THIS AIR LINE')
            ok_got_back(view='validatorsView', obj=f'auth for delete:{auth_update}')

            # customer is not authenticate for updating details
            if auth_update != True:
                
                # error response
                return auth_update
            
            # get user_id from token dictionary    
            airline_user_id = request.session.get('token')['id']
            logger.info(f'OK got airline_token_user_id: {airline_user_id} - HTTP/1.1 200 OK')
            
            # validating data for updating
            valid_airline_data = instance_data.airline_data(request=request, user_id=airline_user_id)

            # if airline data not valid 
            if validator.if_isinstance(valid_airline_data) != False:
                
                # error response
                return valid_airline_data

            # data is valid
            # take out user_id fromdata before updating instance
            valid_airline_data.pop('user_id_id', None)
            
            try:
                # update airline details
                updated_airline = api_update_instance(validated_data=valid_airline_data, id=air_line_id, instance_model=AirLineCompanies, model_serializer=AirlineSerializer)
                
                # success reponse with airline new details or an error response.
                return updated_airline
            
            # handle any exceptions that occur during updating airline details 
            except Exception as e:
                return error_500(e=e, model='AirLinesFacade.update_airline()')
       
        # handle any exceptions that occur during processing this method 
        except Exception as e: 
            return error_500(e=e, model='AirLinesFacade.update_airline()')        

    
    # airline role (2) login require
    @require_role(1,2) 
    # method for adding flight to linked airline
    def add_flight(self, request):
        ok_move_to(model='AirLinesFacade', func='add_flight()')
        
        try:
            # get airline_id by the user_id from token
            air_line_id = get_object_id_by_user_id(request, instance=AirLineCompanies, entity_id='air_line_id')
            ok_got_back(view='operation_funcs.get_airline_id_by_user_id()', obj=f'air_line_id:{air_line_id}' )
            
            # getting and vlidating flight details.
            data = instance_data.flight_data(request=request, air_line_id=air_line_id)
            ok_got_back(view='operation_classes.flight_data()', obj=f'data:{data}' )
            
            # flight data not valid
            if validator.if_isinstance(data) != False:

                # error response
                return data
            
            try:
                # create new flight
                new_flight = api_Create_new(data=data, instance_model=Flights, model_serializer=FlightsSerializer)
                ok_got_back(view='SysApiViews', obj=new_flight)
                
                # success reponse with new flight details or an error response.
                return new_flight
            
            # handle any exceptions that occur during creating flight 
            except Exception as e:
                return error_500(e=e, model='AirLinesFacade')

        # handle any exceptions that occur during processing this method 
        except Exception as e: 
            return error_500(e=e, model='AirLinesFacade.add_flight()')  
    
    
    # airline role (2) login require
    @require_role(2) 
    # method for update flight to linked airline
    def update_flight(self, request, flight_id):
        ok_move_to(model='AirLinesFacade', func='update_flight()')
        
        try:
            # authenticating airline for flight update
            auth_update = validator.valid_user_for_operation(request=request, model=AirLineCompanies, model1=Flights, attr_name='flight_id', id=flight_id, attr_name2='air_line_id', operation='UPDATE THIS FLIGHT')
            ok_got_back(view='validatorsView', obj=f'auth for delete:{auth_update}')
            
            # airline is not authenticate for updating flight
            if auth_update != True:

                # error response                
                return auth_update      
            
            # get the airline_id by user_id            
            air_line_id = get_object_id_by_user_id(request=request, instance=AirLineCompanies, entity_id='air_line_id')
            ok_got_back(view='operation_funcs.get_airline_id_by_user_id()', obj=f'air_line_id:{air_line_id}')
            
            # getting and vlidating flight details.           
            valid_flight_data = instance_data.flight_data(request=request, air_line_id=air_line_id)
            ok_got_back(view='operation_classes.flight_data()', obj=f'valid_flight_data')
            
            # flight data not valid
            if validator.if_isinstance(valid_flight_data) != False:
                
                # error response
                return valid_flight_data
            
            try:
                # update flight 
                updated_flight = api_update_instance(validated_data=valid_flight_data, id=flight_id, instance_model=Flights, model_serializer=FlightsSerializer)
                ok_got_back(view='SysApiViews', obj='updated_flight')
                
                # success reponse with flight new details or an error response.
                return updated_flight
            
            # handle any exceptions that occur during updating flight
            except Exception as e:
                return error_500(e=e, model='AirLinesFacade.update_flight()')

        # handle any exceptions that occur during processing this method 
        except Exception as e: 
                return error_500(e=e, model='AirLinesFacade.update_flight()') 

    
    # airline role (2) login require
    @require_role(2)
    # method for deleting flight to linked airline
    def remove_flight(self, request, flight_id):
        ok_move_to(model='AirLinesFacade', func='remove_flight()')
        
        try:
            # authenticate airline for updating linked flight
            auth_delete = validator.valid_user_for_operation(request=request, model=AirLineCompanies, model1=Flights, attr_name='flight_id', id=flight_id, attr_name2='air_line_id', operation='REMOVE THIS FLIGHT')
            ok_got_back(view='validatorsView', obj=f'auth for delete:{auth_delete}')
            
            # airline is not authenticate for updating flight
            if auth_delete != True:
                
                # error response
                return auth_delete
            
            try:
                # deleting flight
                flight_for_delete = api_delete(id=flight_id, instance_model=Flights)
                ok_got_back(view='SysApiViews', obj='flight_for_delete')
                
                # success response with deleted flight_id or an error response.
                return flight_for_delete
            
            # handle any exceptions that occur during deleting flight 
            except Exception as e:
                return error_500(e=e, model='AirLinesFacade.remove_flight()')
                   
        # handle any exceptions that occur during processing this method 
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade.remove_flight()')