from ...api.SysApiViews import *


class FacadeBase():
    
    # method to get list of all flights
    
    def get_all_flights(self):
        ok_move_to(model='facadebace', func='get_all_flights')
        
        try:
            # get the list via the api view
            flights_list = api_get_list(instance_model=Flights, model_serializer=FlightsSerializer)
            ok_got_back(view='SysApiViews', obj='flights_list')
            
            # response that was received from the api view 
            return flights_list
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacadeBase.get_all_flights()')

    # method for getting flight by the flight_id
    def get_flight_by_id(self, flight_id):
        ok_move_to(model='facadebace', func='get_flight_by_id')

        try:
            # get the flight via the api view
            flight = api_get_object_by_entity_id(id=flight_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='flight_id')
            ok_got_back(view='SysApiViews', obj='flight')
            
            # response that was received from the api view 
            return flight
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_flight_by_id()')

    # method for getting flights list by the origin_country_id
    def get_flights_by_origin_country_id(self, origin_country_id):
        ok_move_to(model='facadebace', func='get_flights_by_origin_country_id')
        
        try:
            # get the list via the api view
            flights = api_get_object_by_entity_id(id=origin_country_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='origin_country_id')
            ok_got_back(view='SysApiViews', obj='flights')
            
            # response that was received from the api view 
            return flights
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_flights_by_origin_country_id()')

    # method for getting list of flights by the destination_country_id
    def get_flights_by_destination_country_id(self, destination_country_id):
        ok_move_to(model='facadebace', func='get_flights_by_destination_country_id')
        
        try:
            # get the list via the api view
            flights = api_get_object_by_entity_id(id=destination_country_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='destination_country_id')
            ok_got_back(view='SysApiViews', obj='flights')
            
            # response that was received from the api view 
            return flights
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_flights_by_destination_country_id()')

    # method for getting list of flights by the departure_date
    def get_flights_by_departure_date(self, date):
        ok_move_to(model='facadebace', func='get_flights_by_departure_date')
        
        try:
            # get the list via the api view
            flights = api_get_flights_by_date(date=date, instance_model=Flights, model_serializer=FlightsSerializer, time_type={'departure_time__date': date})
            ok_got_back(view='SysApiViews', obj='flights')
            
            # response that was received from the api view 
            return flights
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_flights_by_departure_date()')
    
    # method for getting list of flights by the landing_date
    def get_flights_by_landing_date(self, date):
        ok_move_to(model='facadebace', func='get_flights_by_landing_date')
        
        try:
            # get the list via the api view
            flights = api_get_flights_by_date(date=date, instance_model=Flights, model_serializer=FlightsSerializer, time_type={'landing_time__date': date})
            ok_got_back(view='SysApiViews', obj='flights')
            
            # response that was received from the api view 
            return flights
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_flights_by_landing_date()')

    # method for getting flights list by air_line_id
    def get_flights_by_air_line_id(self, air_line_id):
        ok_move_to(model='facadebace', func='get_flights_by_air_line_id')
        
        try:
            # get the list via the api view
            flights = api_get_object_by_entity_id(id=air_line_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='air_line_id')
            ok_got_back(view='SysApiViews', obj='flights')
            
            # response that was received from the api view 
            return flights
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_flights_by_air_line_id()')
    
    # method for get list of next 12 hours arriving flights by the destination_country_id
    def get_arrival_flights(self, destination_country_id):
        ok_move_to(model='facadebace', func='get_arrival_flights')
        
        try:
            # get the list via the api view
            flights = api_get_next_12_hours_flights(entity='landing_time', model_serializer=FlightsSerializer, instance_model=Flights, country_id=destination_country_id, country_type='destination_country_id')
            ok_got_back(view='SysApiViews', obj='flights')
            
            # response that was received from the api view 
            return flights
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_arrival_flights()')

    # method for get list of next 12 hours departure flights by the origin_country_id
    def get_departure_flights(self, origin_country_id):
        ok_move_to(model='facadebace', func='get_departure_flights')
        
        try:
            # get the list via the api view
            flights = api_get_next_12_hours_flights(entity='departure_time', model_serializer=FlightsSerializer, instance_model=Flights, country_id=origin_country_id, country_type='origin_country_id')
            ok_got_back(view='SysApiViews', obj='flights')
            
            # response that was received from the api view 
            return flights
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_departure_flights()')
    
    # method for getting list of all airline companies in system
    def get_all_airlines(self):
        ok_move_to(model='facadebace', func='get_all_airlines')
        
        try:
            # get the list via the api view
            airlines_list = api_get_list(instance_model=AirLineCompanies, model_serializer=AirlineSerializer)
            ok_got_back(view='SysApiViews', obj='airlines_list')
            
            # response that was received from the api view
            return airlines_list 
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_all_airlines()')

    # method for getting airline details by the airline_id
    def get_airline_by_id(self, airline_id):
        ok_move_to(model='facadebace', func='get_airline_by_id')
        
        try:
            # get the details via the api view
            airline = api_get_object_by_entity_id(id=airline_id, instance_model=AirLineCompanies, model_serializer=AirlineSerializer, entity='air_line_id')
            ok_got_back(view='SysApiViews', obj='airline')
            
            # response that was received from the api view
            return airline
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_airline_by_id()')

    # method for getting airline details by the country_id
    def get_airline_by_country_id(self, country_id):
        ok_move_to(model='facadebace', func='get_airline_by_country_id')
        
        try:
            # get the details via the api view
            airline = api_get_object_by_entity_id(id=country_id, instance_model=AirLineCompanies, model_serializer=AirlineSerializer, entity='country_id')
            ok_got_back(view='SysApiViews', obj='airline')
            
            # response that was received from the api view
            return airline
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_airline_by_country_id()')

    # method for getting list of all countries in system
    def get_all_countries(self):
        ok_move_to(model='facadebace', func='get_all_countries')
        
        try:
            # get the list via the api view
            countries_list = api_get_list(instance_model=Countries, model_serializer=CountriesSerializer)
            ok_got_back(view='SysApiViews', obj='airlines_list')
            
            # response that was received from the api view
            return countries_list 
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_all_countries()')
    
    # method for getting country details by the country_by_id
    def get_country_by_id(self, country_id):
        ok_move_to(model='facadebace', func='get_country_by_id')
        
        try:
            # get the details via the api view
            country = api_get_object_by_entity_id(id = country_id, instance_model = Countries, model_serializer = CountriesSerializer, entity='country_id')
            ok_got_back(view='SysApiViews', obj='country')
            
            # response that was received from the api view
            return country
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='FacdeBase.get_country_by_id()')
    
 
    # internal method for creating new user, via "instance_data.new_user_data" for validtaind the received data
    def create_new_user(self, request, user_role):
        ok_move_to(model='facadebase', func='create_new_user')
        
        # take data, validating it, and return dictionary with key/value for validated details
        data = instance_data.new_user_data(request=request, user_role=user_role)
        ok_got_back(view='instance_data', obj='data')
        
        # chek if no error (JsonResponse) received
        if not validator.if_isinstance(data):    
            ok_vlidate_data(model='FacadeBase', func='create_new_user')
            
            try:
                # create new user via the api view
                new_user = api_Create_new(data=data, instance_model=Users, model_serializer=UsersSerializer)
                ok_got_back(view='SysApiViews', obj='new_user')
                
                # response that was received from the api view
                return new_user
            
            # handle any exceptions that occur during processing this method
            except Exception as e:
                return error_500(e=e, model='FacdeBase.create_new_user()')
        
        else:
            # response from api view if error (JsonResponse) received
            return data

    # internal method for deleting user by the user_id
    def delete_user(self, user_id):
        ok_move_to(model='FacadeBase', func='delete_user()')
        
        try:
            # delete user via api view
            user_for_delete = api_delete(id=user_id, instance_model=Users)
            ok_got_back(view='SysApiViews', obj='user_for_delete')
            
            # response that was received from the api view
            return user_for_delete
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')    