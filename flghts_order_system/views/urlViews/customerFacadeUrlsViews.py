from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from ...utils.response_messages.ok_messages import *
from ..facadeViews import *

facade_customer = CustomerFacade()

# decorator to exempt CSRF protection (**for all views at current model**) 
@csrf_exempt
@api_view(['PUT'])
def customer(request, customer_id):
    
    # ensure only PUT requests are allowed
    got_request(request)
    if request.method != 'PUT':
        return error_405(request=request)
    
    try:

        # update customer by cust_id
        updated_customer = facade_customer.update_customer(request=request, customer_id=customer_id)
        ok_got_back(view='CustomerFacade', obj=f'updated_customer:{updated_customer}')
        
        # Successful update response or an error response 
        return updated_customer
    
    # Handle any exceptions that occur during customer update
    except Exception as e:
        return error_500(e=e , model='customerFacadeUrlsViews.customer()')
    
csrf_exempt
@api_view(['POST'])
def tickets(request):

    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'POST':
        return error_405(request=request)

    try: 

        # start ticket ordering process for logged in customer
        new_ticket = facade_customer.add_ticket(request=request)
        ok_got_back(view='CustomerFacade', obj='new_ticket')
        
        # successful ticket creation response or an error response 
        return new_ticket
    
    # handle any exceptions that occur during ticket creation
    except Exception as e:
        return error_500(e=e, model='customerFacadeUrlsViews.tickets()')


csrf_exempt
@api_view(['DELETE'])
def ticket(request, ticket_id):
   
    # ensure only DELETE requests are allowed
    got_request(request)
    if request.method != 'DELETE':
        return error_405(request=request)
    
    try:

        # attempt to delete the ticket for logged-in customer
        ticket_to_remove = facade_customer.remove_ticket(request=request, ticket_id=ticket_id)
        ok_got_back(view='CustomerFacade', obj='ticket_to_remove')
        
        # successful deletion response or an error response 
        return ticket_to_remove
    
    # handle any exceptions during ticket deletion
    except Exception as e:
        return error_500(e=e, model='customerFacadeUrlsViews.ticket()')
   
@csrf_exempt
@api_view(['GET'])
def get_my_tickets(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)

    try:
        
        # get list of flight tickets belonging to logged in customer by the cust_id
        my_tickets = facade_customer.get_my_tickets(request=request)
        ok_got_back(view='CustomerFacade', obj='my_tickets')
        
        # successful response with the list of tickets or an error response 
        return my_tickets
    
    # handle any exceptions that occur while fetching the tickets list
    except Exception as e:
        return error_500(e=e, model='customerFacadeUrlsViews.get_my_tickets()')

@csrf_exempt
@api_view(['GET'])
def customer_by_user_id(request, user_id):  
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET': 
        return error_405(request=request)
    
    try:   
        # get admin details by user id
        customer = facade_customer.customer_details_by_user_id(request=request, user_id=user_id)
        ok_got_back(view='FacadeBase', obj=customer)
        
        # successful response with flight details or an error response
        return customer
    
    except Exception as e:
        return error_500(e=e , model='facadeBaseUrlsViews.flight()')       