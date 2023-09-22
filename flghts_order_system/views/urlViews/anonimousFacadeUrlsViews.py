from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from ...utils.response_messages.ok_messages import *
from ...utils.operation_classes import InstanceData
from ..facadeViews import *
from django.middleware.csrf import get_token


instance_data = InstanceData()
facade_anonymous = AnonymousFacade()


@csrf_exempt
@api_view(['POST'])
def login(request):
    
    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'POST':
        return error_405(request=request)
    
    csrf_token = get_token(request)
    try:
        
        logger.info(f'passed login token: {csrf_token}')
        #data = instance_data.login_data(request=request)
        
        # start login process
        user = facade_anonymous.login(request)#, **data)
        ok_got_back(view='AnonymousFacade', obj=user)
        a = request.session['token']
        logger.info(f'login toke: {str(a)}')
        # successful login response or an error response 
        return user
    
    # handle any exceptions that occur during login
    except Exception as e:
        return error_500(e=e, model='anonimousFacadeUrlsView.login()')
    
        
    
@csrf_exempt
@api_view(['GET'])
def logout(request):
    
    # ensure only GET requests are allowed
    got_request(request)
    if request.method != 'GET':
        return error_405(request=request)
    
    try:
        
        # ckeck if user already looged in
        if check_session_active(request=request) == True:
            
            # Remove the CSRF token from the session
            #del request.session[get_token(request)]
            
            # Logout: end(flush) session
            request.session.flush()
            
            # Successful logout response
            return ok_logout()
            
            # successful login response 
         
        
        # response if session in already not active
        return session_is_active_json(state=' -ERROR- NOT')
    
    # handle any exceptions that occur during logout
    except Exception as e:
        return error_500(e=e , model='anonimousFacadeUrlsView.logout()')

@csrf_exempt   
@api_view(['POST'])
def add_customer(request):

    # ensure only POST requests are allowed
    got_request(request)
    if request.method != 'POST':
        return error_405(request=request)
    
    try:  
        # start customer register process for anonimous user  
        new_customer = facade_anonymous.add_customer(request=request)
        ok_got_back(view='AnonymousFacade', obj='new_customer')
        
        # successful customer registration response or an error response 
        return new_customer
    
    # handle any exceptions that occur during customer registration
    except Exception as e:
        return error_500(e=e, model='anonimousFacadeUrlsView.customers()')
 
        