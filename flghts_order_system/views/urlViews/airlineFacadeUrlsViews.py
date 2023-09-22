from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from ...utils.response_messages.ok_messages import *
from ..facadeViews import *
from loggers.loggers import *

errlogger = errLogger()
logger = lggr()
facade_airline = AirLinesFacade()

@csrf_exempt
@api_view(['GET'])
def get_my_flights(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:
        # get list of flights belonging to logged in airline by the air_line_id
        my_flights = facade_airline.get_my_flights(request=request)
        ok_got_back(view='AirLinesFacade', obj='my_flights')
        
        # successful response with the list of flights or an error response 
        return my_flights
    
    # handle any exceptions that occur while fetching the flights list
    except Exception as e:
        return error_500(e=e, model='airlineFacadeUrlsViews.get_my_flights()')

@csrf_exempt
@api_view(['PUT'])
def airline(request, air_line_id):
    
    # ensure only PUT requests are allowed
    got_request(request)
    if request.method != 'PUT':
        return error_405(request=request)
    
    try:
        # start proccesing airline details update for the logged in airline 
        updated_airline = facade_airline.update_airline(request=request, air_line_id=air_line_id)
        ok_got_back(view='CustomerFacade', obj='updated_airline')
        
        # successful response with the airline details or or an error response
        return updated_airline
    
    # handle any exceptions that occur while updating airline
    except Exception as e:
        return error_500(e=e , model='airlineFacadeUrlsViews.get_my_flights()')       

@csrf_exempt
@api_view(['POST'])   
def add_flight(request):
    
    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'POST':
        return error_405(request=request)
    try:
        # start proccesing flight adding for logged in airline
        new_flight = facade_airline.add_flight(request=request)
        ok_got_back(view='AirLineFacade', obj='new_flight')
        
        # successful response with the new flight details or an error response
        return new_flight
    
    # handle any exceptions that occur while adding flight
    except Exception as e:
        return error_500(e=e, model='airlineFacadeUrlsViews.add_flight()')
 
@csrf_exempt
@api_view(['PUT'])
def update_flight(request, flight_id):
    
    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'PUT':
        return error_405(request=request)
        
    try:
        
        # start proccesing flight updating for logged in airline
        updated_flight = facade_airline.update_flight(request=request, flight_id=flight_id)
        ok_got_back(view='AirLinesFacade', obj='updated_flight')
        
        # successful response with the updated flight details or an error response
        return updated_flight
    
    # handle any exceptions that occur while adding flight
    except Exception as e:
        return error_500(e=e , model='airlineFacadeUrlsViews.update_flight()')  
 
@csrf_exempt
@api_view(['DELETE'])
def remove_flight(request, flight_id):
    
    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'DELETE':
        return error_405(request=request)
        
    try:
        # start proccesing flight deleting for logged in airline
        flight_to_remove = facade_airline.remove_flight(request=request, flight_id=flight_id)
        ok_got_back(view='AirLinesFacade', obj='flight_to_remove')
        
        # successful response for flight deleting or an error response
        return flight_to_remove
    
    # handle any exceptions that occur while deleting flight
    except Exception as e:
        return error_500(e=e, model='airlineFacadeUrlsViews.remove_flight()')

@csrf_exempt
@api_view(['GET'])
def air_line_by_user_id(request, user_id):  
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET': 
        return error_405(request=request)
    
    try:   
        # get airline details by user id
        airline = facade_airline.airline_details_by_user_id(request=request, user_id=user_id)
        ok_got_back(view='FacadeBase', obj=airline)
        
        # successful response with flight details or an error response
        return airline
    
    except Exception as e:
        return error_500(e=e , model='facadeBaseUrlsViews.flight()')           
        