from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..models import UserRole
from ..Serializers import *
from rest_framework.decorators import api_view
from ..loggers import lggr, errLogger
from ..validatorsView import *
from ..messages import *
from .SysApiViews import *
from ..forms import *
from .facadeViews import *

all_requests = [
    'GET',
    'POST',
    'DELETE',
    'PUT', 
    'PATCH', 
    'HEAD',  
    'TRACE', 
    'PROPFIND', 
    ]

logger = lggr()
errlogger = errLogger()
validator= GetValidations()
facade_base = FacadeBase()
facade_administrator = AdministratorFacade()
facade_customer = CustomerFacade()
facade_airline = AirLinesFacade()
facade_anonymous = AnonymousFacade()

class InstanceData():   

    def new_user_data(self, request):
        ok_move_to(model='InstanceData', func='new_user_data')
        new_user_data = request.data
        user_name = new_user_data.get('user_name')
        logger.info(f'O.K user_name status HTTP/1.1 200')
        password = new_user_data.get('password')
        logger.info(f'O.K password status HTTP/1.1 200')
        email = new_user_data.get('email')
        logger.info(f'O.K email status HTTP/1.1 200')
        user_role = new_user_data.get('user_role')
        logger.info(f'O.K user_role status HTTP/1.1 200')
        return {
            'user_name': user_name, 
            'password':password, 
            'email':email, 
            'user_role_id':user_role, 
            }

    def airline_data(self, request):
            airline_data = request.data
            air_line_name = airline_data.get('air_line_name')
            airline_logo = airline_data.get('company_logo')
            country_id = airline_data.get('country_id')
            user_id = airline_data.get('user_id')
            return {'air_line_name': air_line_name, 
                    'company_logo': airline_logo, 
                    'country_id_id': country_id, 
                    'user_id_id': user_id 
                    }
    
    def flight_data(self, request):
            flight_data = request.data
            departure_time = flight_data.get('departure_time')
            landing_time = flight_data.get('landing_time')
            remaining_tickects = flight_data.get('remaining_tickects')
            air_line_id = flight_data.get('air_line_id')
            origin_country_id = flight_data.get('origin_country_id')
            destination_country_id = flight_data.get('destination_country_id')
            return {'departure_time': departure_time, 
                    'landing_time': landing_time, 
                    'remaining_tickects':remaining_tickects,
                    'air_line_id_id':air_line_id, 
                    'origin_country_id_id':origin_country_id, 
                    'destination_country_id_id':destination_country_id    
                    }
    
    def customer_data(self, request):
            ok_move_to(model='InstanceData', func='customer_data')
            customer_data = request.data
            logger.info(f'customer data: {customer_data}')
            cust_first_name = customer_data.get('cust_first_name')
            logger.info(f'cust_first_name: {cust_first_name}')
            cust_last_name = customer_data.get('cust_last_name')
            cust_adress = customer_data.get('cust_adress')
            cust_phone_num = customer_data.get('cust_phone_num')
            cust_credit_card_num = customer_data.get('cust_credit_card_num')
            user_id = customer_data.get('user_id')
            return {
                'cust_first_name': cust_first_name, 
                'cust_last_name': cust_last_name,
                'cust_adress': cust_adress,
                'cust_phone_num': cust_phone_num,
                'cust_credit_card_num': cust_credit_card_num,
                'user_id_id': user_id,
                }

    def ticket_data(self, request):
        ticket_data = request.data
        flight_id = ticket_data.get('flight_id')
        cust_id = ticket_data.get('cust_id')
        return {'flight_id_id': flight_id, 'cust_id_id': cust_id}

    def administrator_data(self, request):
            administrator_data = request.data
            admin_first_name = administrator_data.get('admin_first_name')
            admin_last_name = administrator_data.get('admin_last_name')
            user_id = administrator_data.get('user_id')
            return {
                'admin_first_name': admin_first_name, 
                'admin_last_name': admin_last_name,
                'user_id_id': user_id,
                }







    def countries_data(self, request):
        country_data = request.data
        country_name = country_data.get('country_name')
        country_flag = country_data.get('country_flag')
        return {'country_name': country_name, 'country_flag': country_flag}

    
    def user_role_data(self, request):
        new_user_role_data = request.data
        role_name = new_user_role_data.get('role_name')
        #role_logo = new_user_role_data.get('role_logo')
        return {'role_name': role_name}#, 'role_logo': role_logo}
    
instance_data = InstanceData()














csrf_exempt
@api_view(all_requests)
def flights(request):
    got_request(request)
    if request.method == 'GET':
        try:
            flights = facade_base.get_all_flights()
            ok_got_back(view='FacadeBase', obj='flights list')
            return flights
        except Exception as e:
            return error_500(e=e , model='urlViews')
    elif request.method == 'POST':
        try:   
            data = instance_data.flight_data(request=request)
            ok_got_back(view='instance_data', obj=f'data {data}')
            new_flight = facade_airline.add_flight(data)
            ok_got_back(view='AirLineFacade', obj='new_flight')
            return new_flight
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)
 
@csrf_exempt
@api_view(all_requests)
def flight(request, flight_id):
    got_request(request)
    if request.method == 'GET':
        try:
            flight = facade_base.get_flight_by_id(flight_id)
            ok_got_back(view='FacadeBase', obj='flight')
            return flight
        except Exception as e:
            return error_500(e=e , model='urlViews')
    elif request.method == 'PUT':
        try:
            updated_flight = facade_airline.update_flight(request.data, flight_id=flight_id)
            ok_got_back(view='AirLinesFacade', obj='updated_flight')
            return updated_flight
        except Exception as e:
            return error_500(e=e , model='urlViews')  
    elif request.method == 'DELETE':
        try:
            flight_to_remove = facade_airline.remove_flight(flight_id)
            ok_got_back(view='AirLinesFacade', obj='flight_to_remove')
            return flight_to_remove
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_flights_by_origin_country_id(request, origin_country_id):
    got_request(request)
    if request.method == 'GET':
        try:
            flights = facade_base.get_flights_by_origin_country_id(origin_country_id)
            ok_got_back(view='FacadeBase', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_flights_by_destination_country_id(request, destination_country_id):
    got_request(request)
    if request.method == 'GET':
        try:
            flights = facade_base.get_flights_by_destination_country_id(destination_country_id)
            ok_got_back(view='FacadeBase', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_flights_by_departure_date(request, departure_date):
    got_request(request)
    if request.method == 'GET':
        try:
            flights = facade_base.get_flights_by_departure_date(departure_date)
            ok_got_back(view='FacadeBase', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_flights_by_landing_date(request, landing_date):
    got_request(request)
    if request.method == 'GET':
        try:
            flights = facade_base.get_flights_by_landing_date(landing_date)
            ok_got_back(view='FacadeBase', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)  

@csrf_exempt
@api_view(all_requests)
def get_flights_by_air_line_id(request, air_line_id):
    got_request(request)
    if request.method == 'GET':
        try:
            flights = facade_base.get_flights_by_air_line_id(air_line_id)
            ok_got_back(view='FacadeBase', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_arrival_flights_by_country_id(request, destination_country_id):
    got_request(request)
    if request.method == 'GET':
        try:
            flights = facade_base.get_arrival_flights(destination_country_id)
            ok_got_back(view='FacadeBase', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)   

@csrf_exempt
@api_view(all_requests)
def get_departure_flights_by_country_id(request, origin_country_id):
    got_request(request)
    if request.method == 'GET':
        try:
            flights = facade_base.get_departure_flights(origin_country_id)
            ok_got_back(view='FacadeBase', obj='flights')
            return flights
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request) 

csrf_exempt
@api_view(all_requests)
def airlines(request):
    got_request(request)
    if request.method == 'GET':
        try:
            airlines = facade_base.get_all_airlines()
            ok_got_back(view='FacadeBase', obj='airlines list')
            return airlines
        except Exception as e:
            return error_500(e=e , model='urlViews')
    elif request.method == 'POST':
        try:   
            data = instance_data.airline_data(request=request)
            validator.validate_name(data['air_line_name'])
            ok_got_back(view='instance_data', obj=f'data {data}')
            new_airline = facade_administrator.add_airline(data)
            ok_got_back(view='AirLineFacade', obj='new_airline')
            return new_airline
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_airline_by_id(request, airline_id):
    got_request(request)
    if request.method == 'GET':
        try:
            airline = facade_base.get_airline_by_id(airline_id)
            ok_got_back(view='FacadeBase', obj='airline')
            return airline
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_airline_by_country_id(request, country_id):
    got_request(request)
    if request.method == 'GET':
        try:
            airline = facade_base.get_airline_by_country_id(country_id)
            ok_got_back(view='FacadeBase', obj='airline')
            return airline
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)   

@csrf_exempt
@api_view(all_requests)
def countries(request):
    got_request(request)
    if request.method == 'GET':
        try:
            countries = facade_base.get_all_countries()
            ok_got_back(view='FacadeBase', obj='countries list')
            return countries
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)  

@csrf_exempt
@api_view(all_requests)
def get_country_by_id(request, country_id):
    got_request(request)
    if request.method == 'GET':
        try:
            country = facade_base.get_country_by_id(country_id)
            ok_got_back(view='FacadeBase', obj='country')
            return country
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def users(request):
    got_request(request)
    if request.method == 'POST':
        try:   
            data = instance_data.new_user_data(request=request)
            ok_got_back(view='instance_data', obj='data')
            validator.validate_name(data['user_name'])
            validator.validate_email(data['email'])
            validator.validate_password(data['password'])
            ok_vlidate_data(model='urlview', func='users')
            new_user = facade_base.create_new_user(data)
            ok_got_back(view='FacadeBase', obj='new_user')
            return new_user
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def customers(request):
    got_request(request)
    if request.method == 'GET':
        try:
            customers_list = facade_administrator.get_all_customers()
            ok_got_back(view='FacadeAdministrator', obj='customers_list')
            return customers_list
        except Exception as e:
            return error_500(e=e, model='urlViews')
    elif request.method == 'POST':
        try:   
            data = instance_data.customer_data(request=request)
            ok_got_back(view='instance_data', obj=f'data {data}')
            validator.validate_name(data['cust_first_name'])
            ok_vlidate_data(model='urlview', func='customers')
            new_customer = facade_anonymous.add_customer(data)
            ok_got_back(view='AnonymousFacade', obj='new_customer')
            return new_customer
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def customer(request, customer_id):
    got_request(request)
    if request.method == 'PUT':
        try:
            updated_customer = facade_customer.update_customer(request.data, customer_id=customer_id)
            ok_got_back(view='CustomerFacade', obj='updated_customer')
            return updated_customer
        except Exception as e:
            return error_500(e=e , model='urlViews')
    elif request.method == 'DELETE':
        try:
            customer_to_remove = facade_administrator.remove_customer(customer_id)
            ok_got_back(view='AdministratorFacade', obj='customer_to_remove')
            return customer_to_remove
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

csrf_exempt
@api_view(all_requests)
def tickets(request):
    got_request(request)
    if request.method == 'GET':
        try:
            tickets_list = facade_customer.add_ticket()
            ok_got_back(view='CustomerFacade', obj='tickets_list')
            return tickets_list
        except Exception as e:
            return error_500(e=e, model='urlViews')
    elif request.method == 'POST':
        try:   
            data = instance_data.ticket_data(request=request)
            ok_got_back(view='instance_data', obj=f'data {data}')
            new_ticket = facade_customer.add_ticket(data)
            ok_got_back(view='CustomerFacade', obj='new_ticket')
            return new_ticket
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

csrf_exempt
@api_view(all_requests)
def ticket(request, ticket_id):
    got_request(request)
    if request.method == 'DELETE':
        try:
            ticket_to_remove = facade_customer.remove_ticket(ticket_id)
            ok_got_back(view='CustomerFacade', obj='ticket_to_remove')
            return ticket_to_remove
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_my_tickets(request, cust_id):
    got_request(request)
    if request.method == 'GET':
        try:
            my_tickets = facade_customer.get_my_tickets(cust_id)
            ok_got_back(view='CustomerFacade', obj='my_tickets')
            return my_tickets
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_my_flights(request, air_line_id):
    got_request(request)
    if request.method == 'GET':
        try:
            my_flights = facade_airline.get_my_flights(air_line_id)
            ok_got_back(view='CustomerFacade', obj='my_flights')
            return my_flights
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def airline(request, air_line_id):
    got_request(request)
    if request.method == 'PUT':
        try:
            data = instance_data.airline_data(request=request)
            validator.validate_name(data['air_line_name'])
            updated_airline = facade_airline.update_airline(request.data, air_line_id=air_line_id)
            ok_got_back(view='CustomerFacade', obj='updated_airline')
            return updated_airline
        except Exception as e:
            return error_500(e=e , model='urlViews')
    elif request.method == 'GET':
        try:
            airline = facade_base.get_airline_by_id(id)
            check_error = validator.if_isinstance(airline)
            if check_error == False:
                return status_200_json(object=airline, obj_name='Air Line')
            else:
                return airline
        except Exception as e:
            return error_500(e=e , model='urlViews')
    if request.method == 'DELETE':
        try:
            airline_to_remove = facade_administrator.remove_airline(air_line_id)
            ok_got_back(view='CustomerFacade', obj='airline_to_remove')
            return airline_to_remove
        except Exception as e:
            return error_500(e=e , model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def administrators(request):
    got_request(request)
    if request.method == 'POST':
        try:   
            data = instance_data.administrator_data(request=request)
            ok_got_back(view='instance_data', obj=f'data {data}')
            validator.validate_name(data['admin_first_name'])
            new_administrator = facade_administrator.add_administrator(data)
            ok_got_back(view='AdministratorFacade', obj='new_administrator')
            return new_administrator
        except Exception as e:
            return error_500(e=e, model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def administrator(request, admin_id):
    got_request(request)
    if request.method == 'DELETE':
        try:
            administrator_to_remove = facade_administrator.remove_administrator(admin_id)
            ok_got_back(view='CustomerFacade', obj='airline_to_remove')
            return administrator_to_remove
        except Exception as e:
            return error_500(e=e , model='urlViews')
    else:
        return error_405(request=request)





































    






 

# need validators, logs and exceptions





  






#   elif request.method == 'GET':
#       try:
#           airline = facade_base.get_airline_by_id(id)
#           check_error = validator.if_isinstance(airline)
#           if check_error == False:
#               return status_200_json(object=airline, obj_name='Air Line')
#           else:
#               return airline
#       except Exception as e:
#           return error_500(e=e , model='urlViews')
# 
#   elif request.method == 'DELETE':
#       try:
#           user_role_for_delete = api_delete(
#               id, 
#               instance_model=UserRole
#               )
#           if isinstance(user_role_for_delete, dict) and 'error' in user_role_for_delete:
#               pass
#           else:
#               logger.info('O.K user role successfully deleted HTTP/1.1" 200' )
#               return JsonResponse({'status': 'success', 'deleted user role Id': id}, status=200)
#       except Exception as e:
#           errlogger.error(e)
#           return JsonResponse ({'status': 'ERROR', 'error':str(e)}, status=500)
#   else:
#      return error_405(request=request)






















































        
































@csrf_exempt
@api_view(all_requests)
def cccountries(request):
    logger.info(f'{request.method} request received HTTP/1.1" 100')
    if request.method == 'GET':
        countries_list = facade_base.get_all_countries()
        return countries_list
    ############################################################
    elif request.method == 'POST':
        try:
            data = instance_data.countries_data(request=request)
            validator.validate_name(data['country_name'])
            if data['country_flag']:
                validator.validate_pic_image_no_pic_sizes(data['country_flag'])
            countries = api_Create_new(
                request.data,
                instance_model=Countries,
                model_serializer = CountriesSerializer,
                )
            if isinstance(countries, dict) and 'error' in countries:
                errlogger.error(countries['error'])
                return JsonResponse({'status': 'ERROR', 'error': countries['error']}, status=400)
            else:
                logger.info('O.K new country been created to table HTTP/1.1" 201 ')
                return JsonResponse({'status': 'success', 'user_role': countries}, status=201)
        except Exception as e:
            errlogger.error(e)
            return JsonResponse ({'status': 'ERROR', 'error': str(e)}, status=500)
    ################################################################################################
    else:
        return error_405(request=request)





    

@csrf_exempt
@api_view(all_requests)
def get_airline_by_username(request, username):
    logger.info(f'{request.method} request received HTTP/1.1" 100')
    if request.method == 'GET':
        try:
            validator.validate_name(username)
            logger.info(f'got validate {username} HTTP/1.1" 200')
            airline = facade_base.get_airline_by_username(name=username)
            if isinstance(airline, JsonResponse) and "ERROR" in airline.content.decode("utf-8"):
                return airline
            else:
                logger.info(f'O.K air line successfully received - HTTP/1.1" 200')
                return JsonResponse({'airline': airline}, status=200)
        except Exception as e:
            return error_500(e=e , model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_customer_by_username(request, username):
    logger.info(f'{request.method} request received HTTP/1.1" 100')
    if request.method == 'GET':
        try:
            validator.validate_name(username)
            logger.info(f'got validate {username} HTTP/1.1" 200')
            customers = facade_administrator.get_customer_by_username(name=username)
            if isinstance(customers, JsonResponse) and "ERROR" in customers.content.decode("utf-8"):
                return customers
            else:
                logger.info(f'O.K air line successfully received - HTTP/1.1" 200')
                return JsonResponse({'airline': customers}, status=200)
        except Exception as e:
            return error_500(e=e , model='urlViews')
    else:
        return error_405(request=request)

@csrf_exempt
@api_view(all_requests)
def get_user_by_username(request, username):
    logger.info(f'{request.method} request received HTTP/1.1" 100')
    if request.method == 'GET':
        try:
            validator.validate_name(username)
            logger.info(f'got validate {username} HTTP/1.1" 200')
            customers = facade_administrator.get_customer_by_username(name=username)
            if isinstance(customers, JsonResponse) and "ERROR" in customers.content.decode("utf-8"):
                return customers
            else:
                logger.info(f'O.K air line successfully received - HTTP/1.1" 200')
                return JsonResponse({'airline': customers}, status=200)
        except Exception as e:
            return error_500(e=e , model='urlViews')
    else:
        return error_405(request=request)






























@csrf_exempt
@api_view(all_requests)
def user_role(request):
    
    logger.info(f'{request.method} request received HTTP/1.1" 100')
    if request.method == 'GET':
        try:
            user_role_list = api_get_list(
                instance_model = UserRole,
                model_serializer = UserRoleSerializer
                )
            logger.info('O.K user role list successfully received HTTP/1.1" 200')
            return JsonResponse(user_role_list, safe=False)
        except Exception as e:
            errlogger.error(e)
            return JsonResponse({'status':'ERROR', 'error':str(e)}, status=500)
    elif request.method == 'POST':
        try:
            data = instance_data.user_role_data(request=request)
            validator.validate_name(data['role_name'])
            if data['role_logo']:
                validator.validate_pic_image_no_pic_sizes(data['role_logo'])
            new_user_role = api_Create_new(
                request.data,
                instance_model=UserRole,
                model_serializer = UserRoleSerializer
                )
            if isinstance(new_user_role, dict) and 'error' in new_user_role:
                errlogger.error(new_user_role['error'])
                return JsonResponse({'status': 'ERROR', 'error': new_user_role['error']}, status=400)
            else:
                logger.info('O.K new user role been created HTTP/1.1" 201 ')
                return JsonResponse({'status': 'success', 'user_role': new_user_role}, status=201)
        except Exception as e:
            errlogger.error(e)
            return JsonResponse ({'status': 'ERROR', 'error': str(e)}, status=500)
    else:
        return error_405(request=request)
            

@csrf_exempt
@api_view(all_requests)
def add_multi_user_roles(request):
    logger.info(f'{request.method} request received')
    if request.method == 'POST':
        try:
            data = instance_data.user_role_data(request=request)
            validator.validate_name(data['role_name'])
            if data['role_logo']:
                validator.validate_pic_image_no_pic_sizes(data['role_logo'])
            new_multi_user_roles = api_create_multi(
                request.data,
                model_serializer=UserRoleSerializer, 
                instance_model=UserRole
                )
            if isinstance(new_multi_user_roles, dict) and 'error' in new_multi_user_roles:
                errlogger.error(new_multi_user_roles['error'])
                return JsonResponse({'status': 'ERROR', 'error': new_multi_user_roles['error']}, status=400)
            else:
                logger.info('O.K all new user roles been created HTTP/1.1" 201')
                return JsonResponse({'status': 'success', 'user_roles': new_multi_user_roles}, status=201)
        except Exception as e:
            errlogger.error(e)
            return JsonResponse ({'status': 'ERROR', 'error':str(e)}, status=500)
    else:
        return error_405(request=request)

        
    

    





















def index(request):
    return HttpResponse('OK!!!!!!!!!!!')

def addUserRoleHttpForm(request):
    if request.method=='POST':
        addUserRoleHttpForm(request = request)
        return HttpResponse ('ok!')
    if request.method=='GET':
        form = UserRoleForm(request.GET)
        return render(request=request, template_name='flghts_order_system/userRoleForm.html', context={'form':form})

