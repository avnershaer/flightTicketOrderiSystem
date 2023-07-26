from .SysApiViews import *
from ..models import *
from ..Serializers import *
from ..messages import *
from ..validatorsView import *
from rest_framework.parsers import JSONParser

validator = GetValidations()

def serialize_returned_data(serializer, obj):
    ok_move_to(model='facades', func='serialize_returned_data')
    serialize_data = serializer(obj)
    return serialize_data.data

class FacadeBase():

    def get_all_flights(self):
        ok_move_to(model='facadebace', func='get_all_flights')
        try:
            flights_list = api_get_list(instance_model=Flights, model_serializer=FlightsSerializer)
            ok_got_back(view='SysApiViews', obj='flights_list')
            return flights_list
        except Exception as e:
            return error_500(e=e, model='FacadeBase')
  
    def get_flight_by_id(self, flight_id):
        ok_move_to(model='facadebace', func='get_flight_by_id')
        try:
            flight = api_get_object_by_entity_id(id=flight_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='flight_id')
            ok_got_back(view='SysApiViews', obj='flight')
            return flight
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_flights_by_origin_country_id(self, origin_country_id):
        ok_move_to(model='facadebace', func='get_flights_by_origin_country_id')
        try:
            flights = api_get_object_by_entity_id(id=origin_country_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='origin_country_id')
            ok_got_back(view='SysApiViews', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_flights_by_destination_country_id(self, destination_country_id):
        ok_move_to(model='facadebace', func='get_flights_by_destination_country_id')
        try:
            flights = api_get_object_by_entity_id(id=destination_country_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='destination_country_id')
            ok_got_back(view='SysApiViews', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_flights_by_departure_date(self, date):
        ok_move_to(model='facadebace', func='get_flights_by_departure_date')
        try:
            flights = api_get_flights_by_date(date=date, instance_model=Flights, model_serializer=FlightsSerializer, time_type={'departure_time__date': date})
            ok_got_back(view='SysApiViews', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')
    
    def get_flights_by_landing_date(self, date):
        ok_move_to(model='facadebace', func='get_flights_by_landing_date')
        try:
            flights = api_get_flights_by_date(date=date, instance_model=Flights, model_serializer=FlightsSerializer, time_type={'landing_time__date': date})
            ok_got_back(view='SysApiViews', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_flights_by_air_line_id(self, air_line_id):
        ok_move_to(model='facadebace', func='get_flights_by_air_line_id')
        try:
            flights = api_get_object_by_entity_id(id=air_line_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='air_line_id')
            ok_got_back(view='SysApiViews', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')
    
    def get_arrival_flights(self, destination_country_id):
        ok_move_to(model='facadebace', func='get_arrival_flights')
        try:
            flights = api_get_next_12_hours_flights(entity='landing_time', model_serializer=FlightsSerializer, instance_model=Flights, country_id=destination_country_id, country_type='destination_country_id')
            ok_got_back(view='SysApiViews', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_departure_flights(self, origin_country_id):
        ok_move_to(model='facadebace', func='get_departure_flights')
        try:
            flights = api_get_next_12_hours_flights(entity='departure_time', model_serializer=FlightsSerializer, instance_model=Flights, country_id=origin_country_id, country_type='origin_country_id')
            ok_got_back(view='SysApiViews', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='FacdeBase')
    
    def get_all_airlines(self):
        ok_move_to(model='facadebace', func='get_all_airlines')
        try:
            airlines_list = api_get_list(instance_model=AirLineCompanies, model_serializer=AirlineSerializer)
            ok_got_back(view='SysApiViews', obj='airlines_list')
            return airlines_list 
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_airline_by_id(self, airline_id):
        ok_move_to(model='facadebace', func='get_airline_by_id')
        try:
            airline = api_get_object_by_entity_id(id=airline_id, instance_model=AirLineCompanies, model_serializer=AirlineSerializer, entity='air_line_id')
            ok_got_back(view='SysApiViews', obj='airline')
            return airline
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_airline_by_country_id(self, country_id):
        ok_move_to(model='facadebace', func='get_airline_by_country_id')
        try:
            airline = api_get_object_by_entity_id(id=country_id, instance_model=AirLineCompanies, model_serializer=AirlineSerializer, entity='country_id')
            ok_got_back(view='SysApiViews', obj='airline')
            return airline
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def get_all_countries(self):
        ok_move_to(model='facadebace', func='get_all_countries')
        try:
            countries_list = api_get_list(instance_model=Countries, model_serializer=CountriesSerializer)
            ok_got_back(view='SysApiViews', obj='airlines_list')
            return countries_list 
        except Exception as e:
            return error_500(e=e, model='FacdeBase')
    
    def get_country_by_id(self, country_id):
        ok_move_to(model='facadebace', func='get_country_by_id')
        try:
            country = api_get_object_by_entity_id(id = country_id, instance_model = Countries, model_serializer = CountriesSerializer, entity='country_id')
            ok_got_back(view='SysApiViews', obj='country')
            return country
        except Exception as e:
            return error_500(e=e, model='FacdeBase')

    def create_new_user(self, data):
        ok_move_to(model='facadebace', func='create_new_user')
        try:
            new_user = api_Create_new(data=data, instance_model=Users, model_serializer=UsersSerializer)
            ok_got_back(view='SysApiViews', obj='new_user')
            return new_user
        except Exception as e:
            return error_500(e=e, model='FacdeBase')


class AnonymousFacade():

    def login():
        pass

    def add_customer(self, data):
            ok_move_to(model='AnonymousFacade', func='add_customer')
            try:
                new_customer = api_Create_new(data=data, instance_model=Customers, model_serializer=CustomersSerializer)
                ok_got_back(view='SysApiViews', obj='new_customer')
                return new_customer
            except Exception as e:
                return error_500(e=e, model='AnonymousFacade')


class CustomerFacade(FacadeBase):

    def update_customer(self, validatedData, customer_id):
        ok_move_to(model='CustomerFacade', func='update_customer')
        try:
            #if serialized_data.is_valid():
                #logger.info(f'O.K serialized data is valid HTTP/1.1" 200')
            updated_customer = api_update_instance(validated_data=validatedData, id=customer_id, instance_model=Customers, model_serializer=CustomersSerializer)
            ok_got_back(view='SysApiViews', obj='updated_customer')
            return updated_customer
        except Exception as e: 
                return error_500(e=e, model='CustomerFacade') 

    def add_ticket(self, data):
        ok_move_to(model='CustomerFacade', func='add_ticket')
        try:
            new_ticket = api_Create_new(data=data, instance_model=Tickets, model_serializer=TicketsSerializer)
            ok_got_back(view='SysApiViews', obj='new_customer')
            return new_ticket
        except Exception as e:
            return error_500(e=e, model='CustomerFacade')
        
    def remove_ticket(self, ticket_id):
        ok_move_to(model='CustomerFacade', func='remove_ticket')
        try:
            ticket_for_delete = api_delete(id=ticket_id, instance_model=Tickets)
            ok_got_back(view='SysApiViews', obj='ticket_for_delete')
            return ticket_for_delete
        except Exception as e:
            return error_500(e=e, model='CustomerFacade')

    def get_my_tickets(self, cust_id):
        ok_move_to(model='CustomerFacade', func='get_my_tickets')
        try:
            my_tickets = api_get_object_by_entity_id(id=cust_id, instance_model=Tickets, model_serializer=TicketsSerializer, entity='cust_id')
            ok_got_back(view='SysApiViews', obj='my_tickets')
            return my_tickets
        except Exception as e:
           return error_500(e=e, model='CustomerFacade')

    
class AirLinesFacade(FacadeBase):

    def get_my_flights(self, air_line_id):
        ok_move_to(model='AirLinesFacade', func='get_my_flights')
        try:
            my_flights = api_get_object_by_entity_id(id = air_line_id, instance_model=Flights, model_serializer=FlightsSerializer, entity='air_line_id')
            ok_got_back(view='SysApiViews', obj='my_flights')
            return my_flights
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')

    def update_airline(self, validatedData, air_line_id):
        ok_move_to(model='AirLinesFacade', func='update_airline')
        try:
            updated_airline = api_update_instance(validated_data=validatedData, id=air_line_id, instance_model=AirLineCompanies, model_serializer=AirlineSerializer)
            ok_got_back(view='SysApiViews', obj='update_airline')
            return updated_airline
        except Exception as e: 
                return error_500(e=e, model='AirLinesFacade')        
        
    def add_flight(self, data):
        ok_move_to(model='AirLinesFacade', func='add_flight')
        try:
            new_flight = api_Create_new(data=data, instance_model=Flights, model_serializer=FlightsSerializer)
            ok_got_back(view='SysApiViews', obj=new_flight)
            return new_flight
        except Exception as e:
            return error_500(e=e, model='AirLinesFacade')

    def update_flight(self, validatedData, flight_id):
        ok_move_to(model='AirLinesFacade', func='update_flight')
        try:
            updated_flight = api_update_instance(validated_data=validatedData, id=flight_id, instance_model=Flights, model_serializer=FlightsSerializer)
            ok_got_back(view='SysApiViews', obj='updated_flight')
            return updated_flight
        except Exception as e: 
                return error_500(e=e, model='AirLinesFacade') 

    def remove_flight(self, ticket_id):
        ok_move_to(model='AirLinesFacade', func='remove_flight')
        try:
            flight_for_delete = api_delete(id=ticket_id, instance_model=Flights)
            ok_got_back(view='SysApiViews', obj='flight_for_delete')
            return flight_for_delete
        except Exception as e:
            return error_500(e=e, model='CustomerFacade')
























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

    def get_all_customers(self):
        ok_move_to(model='AdministratorFacade', func='get_all_customers')
        try:
            customers_list = api_get_list(instance_model=Customers, model_serializer = CustomersSerializer)
            ok_got_back(view='SysApiViews', obj='customers_list')
            return customers_list 
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')

    def add_airline(self, data):
        ok_move_to(model='AdministratorFacade', func='add_airline')
        try:
            new_airline = api_Create_new(data=data, instance_model=AirLineCompanies, model_serializer=AirlineSerializer)
            ok_got_back(view='SysApiViews', obj='new_airline')
            return new_airline
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')

    def add_administrator(self, data):
        ok_move_to(model='AdministratorFacade', func='add_administrator')
        try:
            new_administrator = api_Create_new(data=data, instance_model=Adminstrators, model_serializer=AdministratorSerializer)
            ok_got_back(view='SysApiViews', obj='new_administrator')
            return new_administrator
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
    
    def remove_airline(self, airline_id):
        ok_move_to(model='AdministratorFacade', func='remove_airline')  
        try:
            airline_for_delete = api_delete(id=airline_id, instance_model=AirLineCompanies)
            ok_got_back(view='SysApiViews', obj='airline_for_delete')
            return airline_for_delete
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')   
    
    def remove_customer(self, customer_id):
        ok_move_to(model='AdministratorFacade', func='remove_customer')
        try:
            customer_for_delete = api_delete(id=customer_id, instance_model=Customers)
            ok_got_back(view='SysApiViews', obj='customer_for_delete')
            return customer_for_delete
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
    
    def remove_administrator(self, admin_id):
        ok_move_to(model='AdministratorFacade', func='remove_administrator')

        try:
            administrator_for_delete = api_delete(id=admin_id, instance_model=Adminstrators)
            ok_got_back(view='SysApiViews', obj='customer_for_delete')
            return administrator_for_delete
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')



    





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
        
    






