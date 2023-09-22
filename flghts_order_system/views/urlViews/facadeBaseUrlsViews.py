from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from ...utils.response_messages.ok_messages import *
from ..facadeViews import *

facade_base = FacadeBase()

# decorator to exempt CSRF protection (**for all views at current model**) 
@csrf_exempt
@api_view(['GET'])
def flights(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try: 
        # get list of all flights details
        flights = facade_base.get_all_flights()
        ok_got_back(view='FacadeBase', obj='flights list')
        
        # successful response with the list of flights or an error response 
        return flights
    
    except Exception as e:
        return error_500(e=e , model='facadeBaseUrlsViews.flights()')
        
@csrf_exempt
@api_view(['GET'])
def flight(request, flight_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET': 
        return error_405(request=request)
    
    try:    
        # get flight details by the flight id
        flight = facade_base.get_flight_by_id(flight_id)
        ok_got_back(view='FacadeBase', obj='flight')
        
        # successful response with flight details or an error response
        return flight
    
    except Exception as e:
        return error_500(e=e , model='facadeBaseUrlsViews.flight()')
    
@csrf_exempt
@api_view(['GET'])
def get_flights_by_origin_country_id(request, origin_country_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:    
        # get list of flights details by the id of the origin country
        flights = facade_base.get_flights_by_origin_country_id(origin_country_id)
        ok_got_back(view='FacadeBase', obj='flights')
        
        # successful response with flights details or an error response
        return flights
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_flights_by_origin_country_id()')

@csrf_exempt
@api_view(['GET'])
def get_flights_by_destination_country_id(request, destination_country_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try: 
        # get list of flights details by the id of the destination country
        flights = facade_base.get_flights_by_destination_country_id(destination_country_id)
        ok_got_back(view='FacadeBase', obj='flights')
        
        # successful response with flights details or an error response
        return flights
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_flights_by_destination_country_id()')

@csrf_exempt
@api_view(['GET'])
def get_flights_by_departure_date(request, departure_date):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:
        # get list of flights details by the departure date
        flights = facade_base.get_flights_by_departure_date(departure_date)
        ok_got_back(view='FacadeBase', obj='flights')
        
        # successful response with flights details or an error response
        return flights
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_flights_by_departure_date()') 

@csrf_exempt
@api_view(['GET'])
def get_flights_by_landing_date(request, landing_date):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)  
    
    try:
        # get list of flights details by the landing date
        flights = facade_base.get_flights_by_landing_date(landing_date)
        ok_got_back(view='FacadeBase', obj='flights')
        
        # successful response with flights details or an error response
        return flights
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_flights_by_landing_date()') 

@csrf_exempt
@api_view(['GET'])
def get_flights_by_air_line_id(request, air_line_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:
        # get list of flights details by air line_id
        flights = facade_base.get_flights_by_air_line_id(air_line_id)
        ok_got_back(view='FacadeBase', obj='flights')
        
        # successful response with flights details or an error response
        return flights
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_flights_by_air_line_id()')
       
@csrf_exempt
@api_view(['GET'])
def get_arrival_flights_by_country_id(request, destination_country_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:
        # get list of arrivel flights details by country id
        flights = facade_base.get_arrival_flights(destination_country_id)
        ok_got_back(view='FacadeBase', obj='flights')
        
        # successful response with flights details or an error response
        return flights
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_arrival_flights_by_country_id()')

@csrf_exempt
@api_view(['GET'])
def get_departure_flights_by_country_id(request, origin_country_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request) 
    
    try:
        # get list of departure flights details by country id
        flights = facade_base.get_departure_flights(origin_country_id)
        ok_got_back(view='FacadeBase', obj='flights')
        
        # successful response with flights details or an error response
        return flights
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_departure_flights_by_country_id()')
    
csrf_exempt
@api_view(['GET'])
def airlines(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:
        # get list of all air lines details
        airlines = facade_base.get_all_airlines()
        ok_got_back(view='FacadeBase', obj='airlines list')
        
        # successful response with airlines details or an error response
        return airlines
    
    except Exception as e:
        return error_500(e=e , model='facadeBaseUrlsViews.airlines()')
  
@csrf_exempt
@api_view(['GET'])
def get_airline_by_id(request, airline_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
        
    try:
        # get airline details by air_line_id
        airline = facade_base.get_airline_by_id(airline_id)
        ok_got_back(view='FacadeBase', obj='airline')
        
        # successful response with airline details or an error response
        return airline
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_airline_by_id()')

@csrf_exempt
@api_view(['GET'])
def get_airline_by_country_id(request, country_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
        
    try:
        # get airline details by the country_id of airline.
        airline = facade_base.get_airline_by_country_id(country_id)
        ok_got_back(view='FacadeBase', obj='airline')
        
        # successful response with airline details or an error response
        return airline
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_airline_by_country_id()')       

@csrf_exempt
@api_view(['GET'])
def countries(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
        
    try:
        # get list of all countries in system
        countries = facade_base.get_all_countries()
        ok_got_back(view='FacadeBase', obj='countries list')
        
        # successful response with countries details or an error response
        return countries
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_airline_by_country_id()')

          

@csrf_exempt
@api_view(['GET'])
def get_country_by_id(request, country_id):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:
        # get country details by the country_id
        country = facade_base.get_country_by_id(country_id)
        ok_got_back(view='FacadeBase', obj='country')
        
        # successful response with countriy details or an error response
        return country
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.get_country_by_id()')
  
@csrf_exempt
@api_view(['GET']) #*********************************************
def users(request):#**********************************************
    
    # ensure only GET requests are allowed
    got_request(request)#*******************************************
    if request.method != 'POST':
        return error_405(request=request)
    try: 
        # create new user   
        new_user = facade_base.create_new_user(request=request)
        ok_got_back(view='FacadeBase', obj='new_user')
        
        # successful response for new user or an error response
        return new_user
    
    except Exception as e:
        return error_500(e=e, model='facadeBaseUrlsViews.users()')

