from .SysApiViews import *
from ..models import *
from ..Serializers import *
from ..messages import *
from ..validatorsView import *
from rest_framework.parsers import JSONParser

validator = GetValidations()


class FacadeBase():

    def get_all_flights(self):
        try:
            flights_list = api_get_list(
                instance_model = Flights,
                model_serializer = FlightsSerializer,
                )
            check_error = validator.if_isinstance(flights_list)
            if check_error == False:
                return ok_status_200(object=flights_list, obj_name='Flights List')
            else:
                return flights_list 
        except Exception as e:
            return error_500(e=e, model='FacdeBase')
  
    def get_flight_by_id(self, flight_id):
            try:
                flight = api_get_object_by_entity_id(
                    id = flight_id, 
                    instance_model = Flights, 
                    model_serializer = FlightsSerializer, 
                    entity = 'flight_id'
                    )
                check_error = validator.if_isinstance(flight)
                if check_error == False:
                    return ok_status_200(object=flight, obj_name='Flight')
                else:
                    return flight
            except Exception as e:
                return error_500(e=e, model='FacdeBase')

    def get_flights_by_origin_country_id(self, origin_country_id):
        try:
            flights = api_get_object_by_entity_id(
                id = origin_country_id, 
                instance_model = Flights, 
                model_serializer = FlightsSerializer, 
                entity = 'origin_country_id'
                )
            check_error = validator.if_isinstance(flights)
            if check_error == False:
                return ok_status_200(object=flights, obj_name='Flights List')
            else:
                return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_flights_by_destination_country_id(self, destination_country_id):
        try:
            flights = api_get_object_by_entity_id(
                id = destination_country_id, 
                instance_model = Flights, 
                model_serializer = FlightsSerializer, 
                entity = 'destination_country_id'
                )
            check_error = validator.if_isinstance(flights)
            if check_error == False:
                return ok_status_200(object=flights, obj_name='Flights List')
            else:
                return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_flights_by_date(self, date):
        try:
            flight = api_get_flights_by_date(
                date = date,
                instance_model = Flights, 
                model_serializer = FlightsSerializer,
            )
            check_error = validator.if_isinstance(flight)
            if check_error == False:
                return ok_status_200(object=flight, obj_name='Flights List')
            else:
                return flight
        except Exception as e:
            return error_500(e=e, model='FacdeBase')
    
    def get_flights_by_air_line_id(self, air_line_id):
            try:
                flights = api_get_object_by_entity_id(
                    id = air_line_id, 
                    instance_model = Flights, 
                    model_serializer = FlightsSerializer, 
                    entity = 'air_line_id'
                    )
                check_error = validator.if_isinstance(flights)
                if check_error == False:
                    return ok_status_200(object=flights, obj_name='Flights List')
                else:
                    return flights
            except Exception as e:
                return error_500(e=e, model='FacdeBase')
    
    def get_arrival_flights(self, destination_country_id):
            try:
                flights = api_get_last_12_hours_flights( 
                    entity = 'landing_time',
                    model_serializer = FlightsSerializer,
                    instance_model = Flights, 
                    country_id = destination_country_id,
                    country_type = 'destination_country_id'
                    )
                check_error = validator.if_isinstance(flights)
                if check_error == False:
                    return ok_status_200(object=flights, obj_name='Flights List')
                else:
                    return flights
            except Exception as e:
                return error_500(e=e, model='FacdeBase')

    def get_departure_flights(self, origin_country_id):
            try:
                flights = api_get_last_12_hours_flights(
                    entity='departure_time',
                    model_serializer=FlightsSerializer,
                    instance_model=Flights,
                    country_id=origin_country_id,
                    country_type='origin_country_id'
                    )
                check_error = validator.if_isinstance(flights)
                if check_error == False:
                    return ok_status_200(object=flights, obj_name='Flights List')
                else:
                    return flights
            except Exception as e:
                return error_500(e=e, model='FacdeBase')

    def get_all_airlines(self):
        try:
            airlines_list = api_get_list(
                instance_model = AirLineCompanies,
                model_serializer = AirlineSerializer,
                )
            check_error = validator.if_isinstance(airlines_list)
            if check_error == False:
                return ok_status_200(object=airlines_list, obj_name='Air Lines List')
            else:
                return airlines_list 
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_airline_by_id(self, airline_id):
            try:
                airline = api_get_object_by_entity_id(
                    id = airline_id, 
                    instance_model = AirLineCompanies, 
                    model_serializer = AirlineSerializer, 
                    entity = 'air_line_id'
                    )
                check_error = validator.if_isinstance(airline)
                if check_error == False:
                    return ok_status_200(object=airline, obj_name='Air Line')
                else:
                    return airline
            except Exception as e:
                return error_500(e=e, model='FacdeBase')

    def get_airline_by_country_id(self, country_id):
        try:
            airline = api_get_object_by_entity_id(
                id = country_id, 
                instance_model = AirLineCompanies, 
                model_serializer = AirlineSerializer, 
                entity = 'country_id'
                )
            check_error = validator.if_isinstance(airline)
            if check_error == False:
                return ok_status_200(object=airline, obj_name='Air Line')
            else:
                return airline
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_all_countries(self):
        try:
            countries_list = api_get_list(
                instance_model = Countries,
                model_serializer = CountriesSerializer,
                )
            check_error = validator.if_isinstance(countries_list)
            if check_error == False:
                return ok_status_200(object=countries_list, obj_name='Air Lines List')
            else:
                return countries_list 
        except Exception as e:
            return error_500(e=e, model='FacdeBase')
  
    def get_country_by_id(self, country_id):
            try:
                country = api_get_object_by_entity_id(
                    id = country_id, 
                    instance_model = Countries, 
                    model_serializer = CountriesSerializer, 
                    entity = 'country_id'
                    )
                check_error = validator.if_isinstance(country)
                if check_error == False:
                    return ok_status_200(object=country, obj_name='Air Line')
                else:
                    return country
            except Exception as e:
                return error_500(e=e, model='FacdeBase')

    def create_new_user(self, data):
        try:
            
            logger.info(f'OK GOT VALIDATE 2 DATA FACADEVIEWS {data}')
            new_user = api_Create_new( 
                data = data, 
                instance_model = Users,
                model_serializer = UsersSerializer,
            )
            check_error = validator.if_isinstance(new_user)
            if check_error == False:
                serializer = UsersSerializer(new_user)
                return serializer.data
            else:
                return new_user
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    






class AirLinesFacade(FacadeBase):

    def get_my_flights_air_line_id(self, air_line_id):
        ok_move_to(model='AirLinesFacade')
        try:
            my_flights = api_get_object_by_entity_id(
            id = air_line_id,
            instance_model = Flights,
            model_serializer = FlightsSerializer,
            entity = 'air_line_id'
            )
            check_error = validator.if_isinstance(my_flights)
            if check_error == False:
                return ok_status_200(object=my_flights, obj_name='My Flghts')
            return my_flights
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')

    def update_airline(self, validatedData, airline_id):
        ok_move_to(model='AirLinesFacade')
        try:
            serialized_data = AirlineSerializer(data=validatedData)
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')
        logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1" 200')
        try:
            if serialized_data.is_valid():
                logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
                updated_airline = api_update_instance(
                validated_data = serialized_data,
                id = airline_id, 
                instance_model = AirLineCompanies, 
                )
                logger.info(f'got updated_airline from db: {updated_airline} HTTP/1.1" 200')
                check_error = validator.if_isinstance(updated_airline)
                if check_error == False:
                    try:
                        return serialize_data(AirlineSerializer, objects=updated_airline)
                    except Exception as e:
                        return error_500(e=serialized_data.errors, model='AirLinesFacade' )
                else:
                    return updated_airline
        except Exception as e: 
                return error_500(e=e, model='AirLinesFacade')        
        
    def add_flight(self, data):
        ok_move_to(model='AirLinesFacade')
        logger.info(f'O.K got DETAILS {data} HTTP/1.1" 200')
        try:
            serialized_data = FlightsSerializer(data=data)
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')
        logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1" 200')
        try:
           #air_line_id = data['air_line_id']
           #air_line_instance = AirLineCompanies.objects.get(air_line_id=air_line_id)
           #data['air_line_id'] = air_line_instance
           #country_id = data['origin_country_id']
           #country_instance = Countries.objects.get(country_id=country_id)
           #data['origin_country_id'] = country_instance
           #country_id = data['destination_country_id']
           #country_instance = Countries.objects.get(country_id=country_id)
           #data['destination_country_id'] = country_instance
            if serialized_data.is_valid():
                logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
                new_flight = api_Create_new(
                data = serialized_data, 
                instance_model = Flights, 
                model_serializer = FlightsSerializer
                )
                logger.info(f'OK GOT back the new obj from apiview: {new_flight}')
                #check_error = validator.if_isinstance(new_flight)
                #if check_error == False:
                serializer = FlightsSerializer(new_flight)
                logger.info(f'OK GOT  new flight:{serializer}')
                return serializer.data
            else:
                    return serialized_data.errors
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')

    def update_flight(self, validatedData, flight_id):
        ok_move_to(model='AirLinesFacade')
        try:
            serialized_data = FlightsSerializer(data=validatedData)
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')
        logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1" 200')
        try:
            if serialized_data.is_valid():
                logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
                updated_flight = api_update_instance(
                validated_data = serialized_data,
                id = flight_id, 
                instance_model = Flights, 
                )
                logger.info(f'got updated_flight from db: {updated_flight} HTTP/1.1" 200')
                check_error = validator.if_isinstance(updated_flight)
                if check_error == False:
                    try:
                        return serialize_data(FlightsSerializer, objects=updated_flight)
                    except Exception as e:
                        return error_500(e=e+serialized_data.errors, model='AirLinesFacade' )
                else:
                    return updated_flight
        except Exception as e: 
                return error_500(e=e, model='AirLinesFacade') 












    def get_airline_by_username(self, name):
        try:
            air_line = api_get_object_by_username(
                name=name, 
                instance_model=AirLineCompanies, 
                model_serializer = AirlineSerializer,
                )
            if isinstance(air_line, JsonResponse) and 'ERROR' in air_line.content.decode('utf-8'):
                return air_line
            else:
                logger.info(f'O.K got airline -  HTTP/1.1" 200')
                return air_line
        except Exception as e:
            return error_500(e=e, model='Facade Base')

    
        
    


















class AdministratorFacade(FacadeBase):

    def get_customer_by_username(self, name):
        ok_move_to(model='AdministratorFacade')
        try:
            customer = api_get_object_by_username(
                name=name, 
                instance_model=Customers, 
                model_serializer = CustomersSerializer,
                )
            if isinstance(customer, JsonResponse) and 'ERROR' in customer.content.decode('utf-8'):
                return customer
            else:
                logger.info(f'O.K got customer -  HTTP/1.1" 200')
                return customer
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')

    def add_airline(self, data):
        ok_move_to(model='AdministratorFacade')
        logger.info(f'O.K got DETAILS {data} HTTP/1.1" 200')
        try:
            serialized_data = AirlineSerializer(data=data)
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
        logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1" 200')
        try:
            if serialized_data.is_valid():
                logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
                new_airline = api_Create_new(
                data = serialized_data, 
                instance_model = AirLineCompanies, 
                model_serializer = AirlineSerializer
                )
                logger.info(f'OK GOT back the new obj from apiview: {new_airline}')
                #check_error = validator.if_isinstance(new_ticket)
                #if check_error == False:
                #try:
                serializer = AirlineSerializer(new_airline)
                return serializer.data
                #except Exception as e:
                #    return error_500(e=e, model='AdministratorFacade')
                #return new_airline
            else:
                return error_500(e=serialized_data.errors, model='AdministratorFacade' )          
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
        
    def add_customer(self, data):
            ok_move_to(model='AdministratorFacade')
            logger.info(f'O.K got DETAILS {data} HTTP/1.1" 200')
            try:
                serialized_data = CustomersSerializer(data=data)
            except Exception as e:
                return error_500(e=e, model='AdministratorFacade')
            logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1" 200')
            try:
                if serialized_data.is_valid():
                    logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
                    new_customer = api_Create_new(
                    data = serialized_data, 
                    instance_model = Customers, 
                    model_serializer = CustomersSerializer
                    )
                    logger.info(f'OK GOT back the new obj from apiview: {new_customer}')
                    #check_error = validator.if_isinstance(new_ticket)
                    #if check_error == False:
                    #try:
                    serializer = CustomersSerializer(new_customer)
                    return serializer.data
                    #except Exception as e:
                    #    return error_500(e=e, model='AdministratorFacade')
                    #return new_airline
                else:
                    return error_500(e=serialized_data.errors, model='AdministratorFacade' )
            except Exception as e:
                return error_500(e=e, model='AdministratorFacade')

    def add_administrator(self, data):
        ok_move_to(model='AdministratorFacade')
        logger.info(f'O.K got DETAILS {data} HTTP/1.1" 200')
        try:
            serialized_data = AdministratorSerializer(data=data)
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
        logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1" 200')
        try:
            if serialized_data.is_valid():
                logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
                new_administrator = api_Create_new(
                data = serialized_data, 
                instance_model = Adminstrators, 
                model_serializer = AdministratorSerializer
                )
                logger.info(f'OK GOT back the new obj from apiview: {new_administrator}')
                #check_error = validator.if_isinstance(new_ticket)
                #if check_error == False:
                #try:
                serializer = AdministratorSerializer(new_administrator)
                return serializer.data
                #except Exception as e:
                #    return error_500(e=e, model='AdministratorFacade')
                #return new_airline
            else:
                return error_500(e=serialized_data.errors, model='AdministratorFacade' )          
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')

    def remove_airline(self, airline_id):
        ok_move_to(model='AdministratorFacade')
        logger.info(f'O.K got DETAILS {airline_id} HTTP/1.1" 200')
        try:
            airline_for_delete = api_delete(
            id = airline_id, 
            instance_model = AirLineCompanies, 
            )
            logger.info(f'OK GOT back the deleted obj from apiview{airline_for_delete}')
            #check_error = validator.if_isinstance(new_ticket)
            #if check_error == False:
            return airline_for_delete
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
    
    def remove_customer(self, customer_id):
        ok_move_to(model='AdministratorFacade')
        logger.info(f'O.K got DETAILS {customer_id} HTTP/1.1" 200')
        try:
            customer_for_delete = api_delete(
            id = customer_id, 
            instance_model = Customers, 
            )
            logger.info(f'OK GOT back the deleted obj from apiview{customer_for_delete}')
            #check_error = validator.if_isinstance(new_ticket)
            #if check_error == False:
            return customer_for_delete
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
        
    def remove_administrator(self, admin_id):
        ok_move_to(model='AdministratorFacade')
        logger.info(f'O.K got DETAILS {admin_id} HTTP/1.1" 200')
        try:
            administrator_for_delete = api_delete(
            id = admin_id, 
            instance_model = Adminstrators, 
            )
            logger.info(f'OK GOT back the deleted obj from apiview{administrator_for_delete}')
            #check_error = validator.if_isinstance(new_ticket)
            #if check_error == False:
            return administrator_for_delete
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')






    def get_user_by_username(self, name):
        ok_move_to(model='AdministratorFacade')
        try:
            customer = api_get_object_by_username(
                name=name, 
                instance_model=Users, 
                model_serializer = CustomersSerializer,
                )
            if isinstance(customer, JsonResponse) and 'ERROR' in customer.content.decode('utf-8'):
                return customer
            else:
                logger.info(f'O.K got customer -  HTTP/1.1" 200')
                return customer
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
        
    def get_all_customers(self):
        ok_move_to(model='AdministratorFacade')
        try:
            customers_list = api_get_list(
                instance_model = Customers,
                model_serializer = CustomersSerializer,
                )
            check_error = validator.if_isinstance(customers_list)
            if check_error == False:
                ok_chek_error_is_false(model='AdministratorFacade')
                return ok_status_200(object=customers_list, obj_name='Customers List')
            else:
                return customers_list 
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')







class CustomerFacade(FacadeBase):

    def get_my_tickets(self, cust_id):
           try:
               tickets = api_get_object_by_entity_id(
                   id = cust_id, 
                   instance_model = Tickets, 
                   model_serializer = TicketsSerializer, 
                   entity = 'cust_id'
                   )
               if isinstance(tickets, JsonResponse) and "ERROR" in tickets.content.decode("utf-8"):
                   return tickets
               else:
                   logger.info(f'O.K flight successfully received HTTP/1.1" 200')
                   return tickets
           except Exception as e:
               return error_500(e=e, model='AdministratorFacade')

    def update_customer(self, validatedData, customer_id):
        ok_move_to(model='CustomerFacade')
        logger.info(f'O.K got DETAILS {validatedData} HTTP/1.1" 200')
        try:
            serialized_data = CustomersSerializer(data=validatedData)
        except Exception as e:
            return error_500(e=e, model='CustomerFacade')
        logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1" 200')
        try:
            if serialized_data.is_valid():
                logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
                updated_customer = api_update_instance(
                validated_data = serialized_data,
                id = customer_id, 
                instance_model = Customers, 
                )
                logger.info(f'got updated_customer from db: {updated_customer} HTTP/1.1" 200')
                check_error = validator.if_isinstance(updated_customer)
                if check_error == False:
                    try:
                        return serialize_data(CustomersSerializer, objects=updated_customer)
                    except Exception as e:
                        return error_500(e=serialized_data.errors, model='CustomerFacade' )
                else:
                    return serialized_data.errors
            else:
                    return serialized_data.errors
        except Exception as e: 
                return error_500(e=e, model='CustomerFacade') 
        
    def add_ticket(self, data):
        ok_move_to(model='CustomerFacade')
        logger.info(f'O.K got DETAILS {data} HTTP/1.1" 200')
        try:
            serialized_data = TicketsSerializer(data=data)
        except Exception as e:
            return error_500(e=e, model='CustomerFacade')
        logger.info(f'O.K got serialzed data {serialized_data} HTTP/1.1" 200')
        try:
            if serialized_data.is_valid():
                logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
                new_ticket = api_Create_new(
                data = serialized_data, 
                instance_model = Tickets, 
                model_serializer = TicketsSerializer
                )
                logger.info(f'OK GOT back the new obj from apiview: {new_ticket}')
                #check_error = validator.if_isinstance(new_ticket)
                #if check_error == False:
                serializer = TicketsSerializer(new_ticket)
                return serializer.data
            else:
                return serialized_data.errors
          
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')
        
    def remove_ticket(self, ticket_id):
        ok_move_to(model='CustomerFacade')
        logger.info(f'O.K got DETAILS {ticket_id} HTTP/1.1" 200')
        try:
            ticket_for_delete = api_delete(
            id = ticket_id, 
            instance_model = Tickets, 
            )
            logger.info(f'OK GOT back the deleted obj from apiview{ticket_for_delete}')
            #check_error = validator.if_isinstance(new_ticket)
            #if check_error == False:
            return ticket_for_delete
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')
           