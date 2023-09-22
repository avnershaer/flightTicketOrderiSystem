from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from ...utils.response_messages.ok_messages import *
from ..facadeViews import *

facade_administrator = AdministratorFacade()

@csrf_exempt
@api_view(['GET'])
def customers(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)

    try:
        # get list of all customers 
        customers_list = facade_administrator.get_all_customers(request)
        ok_got_back(view='FacadeAdministrator', obj='customers_list')
        
        # successful response with the list of customers or an error response 
        return customers_list
    
    # handle any exceptions that occur while fetching the customers list
    except Exception as e:
        return error_500(e=e, model='urlViews')

csrf_exempt
@api_view(['POST'])
def add_airline(request):

    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'POST':
        return error_405(request=request) 
        
    try:
        # start proccesing airline adding
        new_airline = facade_administrator.add_airline(request=request)
        ok_got_back(view='AirLineFacade', obj='new_airline')
        
        # successful response with airline details or an error response 
        return new_airline
    
    # handle any exceptions that occur while adding airline
    except Exception as e:
        return error_500(e=e, model='administartorFacadeUrlsViews.add_airline()')
  

@csrf_exempt
@api_view(['POST'])
def administrators(request):
    
    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'POST':
        return error_405(request=request) 

    try:
        # start proccesing administrator adding
        new_administrator = facade_administrator.add_administrator(request=request)
        ok_got_back(view='AdministratorFacade', obj='new_administrator')
        
        # successful response with administrator details or an error response 
        return new_administrator
    
    # handle any exceptions that occur while adding airline
    except Exception as e:
        return error_500(e=e, model='administartorFacadeUrlsViews.administrators()')
          
@csrf_exempt
@api_view(['PUT'])
def administrator(request, admin_id):
    
    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'PUT':
        return error_405(request=request)
        
    try:
        # start proccesing administrator updating by admin_id
        updated_admin = facade_administrator.update_administrator(request=request, admin_id=admin_id)
        ok_got_back(view='AdministratorFacade', obj='updated_admin')
        
        # successful response with administrator details or an error response
        return updated_admin
    
    # handle any exceptions that occur while updating admin 
    except Exception as e:
        return error_500(e=e , model='administartorFacadeUrlsViews.administrator()')
    
@csrf_exempt
@api_view(['DELETE'])
def remove_airline(request, air_line_user_id):
    
    # ensure only DELETE requests are allowed
    got_request(request)
    if request.method != 'DELETE':
        return error_405(request=request)
    
    try:
        # start proccesing airline deleting by airline_id
        airline_to_remove = facade_administrator.remove_airline(request=request, air_line_user_id=air_line_user_id)
        ok_got_back(view='CustomerFacade', obj='airline_to_remove')
        
        # successful response for airline deleting or an error response
        return airline_to_remove
    
    # handle any exceptions that occur while updating admin 
    except Exception as e:
        return error_500(e=e , model='administartorFacadeUrlsViews.remove_airline()')
   
@csrf_exempt
@api_view(['DELETE'])
def remove_customer(request, customer_id_user_id):

    # ensure only DELETE requests are allowed
    got_request(request) 
    if request.method != 'DELETE':
        return error_405(request=request)      
        
    try:
        # start proccesing customer deleting by customer_id
        customer_to_remove = facade_administrator.remove_customer(request=request, customer_id_user_id=customer_id_user_id)
        ok_got_back(view='AdministratorFacade', obj='customer_to_remove')
        
        # successful response for customer deleting or an error response
        return customer_to_remove
    
    # handle any exceptions that occur while updating admin
    except Exception as e:
        return error_500(e=e, model='administartorFacadeUrlsViews.remove_customer()')

@csrf_exempt
@api_view(['DELETE'])
def remove_administrator(request, admin_id):
    
    # ensure only DELETE requests are allowed
    got_request(request)
    if request.method != 'DELETE':
        return error_405(request=request)
    
    try:
        # start proccesing administrator deleting by admin_id
        administrator_to_remove = facade_administrator.remove_administrator(request=request, admin_id=admin_id)
        ok_got_back(view='AdministratorFacade', obj='administrator_to_remove')
        
        # successful response for administrator deleting or an error response
        return administrator_to_remove
    
    # handle any exceptions that occur while updating admin
    except Exception as e:
        return error_500(e=e , model='administartorFacadeUrlsViews.remove_administrator()')
         
csrf_exempt
@api_view(['GET'])
def get_all_tickets(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:
        # get list of all tickets in the system of all airlines
        tickets_list = facade_administrator.get_all_tickets(request)
        ok_got_back(view='CustomerFacade', obj='tickets_list')
        
        # successful response whith all tickets details list or an error response
        return tickets_list
    
    # handle any exceptions that occur while updating admin
    except Exception as e:
        return error_500(e=e, model='urlViews')
    
@csrf_exempt
@api_view(['GET'])
def admin_by_user_id(request, user_id):  
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET': 
        return error_405(request=request)
    
    try:   
        # get admin details by user id
        admin = facade_administrator.admin_details_by_user_id(request=request, user_id=user_id)
        ok_got_back(view='FacadeBase', obj=admin)
        
        # successful response with flight details or an error response
        return admin
    
    except Exception as e:
        return error_500(e=e , model='facadeBaseUrlsViews.flight()')      
    
@csrf_exempt
@api_view(['GET'])
def administrators_list(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)

    try:
        # get list of all administrators  
        administrators_list = facade_administrator.get_all_administrators(request)
        ok_got_back(view='FacadeAdministrator', obj='administrators_list')
        
        # successful response with the list of customers or an error response 
        return administrators_list
    
    # handle any exceptions that occur while fetching the customers list
    except Exception as e:
        return error_500(e=e, model='urlViews')