from .facadeBaseViews import FacadeBase
from ...api.SysApiViews import *
from ...api.Serializers import UsersSerializer

validator = GetValidations()


class AnonymousFacade(FacadeBase):

    # init the token
    def __init__(self, token=None):
        self.token = token

    # login user method
    def login(self, request):
        ok_move_to(model='anonymousFacadeViews', func='login()')
        
        try:
            # validate the data received user login data before starting login process,
            # and return dictionary with key/value for validated details
            data = instance_data.login_data(request=request)
            ok_got_back(view='instance_data.login_data', obj=data)
            
            # check if no errors returned (FALSE) 
            if validator.if_isinstance(data) != False:
                
                # error response
                return data 
            
            # check if there is active session before starting login process
            active_session = check_session_active(request)
            ok_got_back(view='operation_funcs', obj=active_session)

            # session is already active (TRUE)
            if active_session is True:
                
                #if user already logged in
                return already_logged_in()
            
            # get the user by username
            user = api_get_object_by_username(name=data['username'], model_serializer=UsersSerializer, instance_model=Users)
            ok_got_back(view='SysapiViews', obj=user)

            # check if no errors returned (FALSE) 
            if validator.if_isinstance(user) != False:
                
                # error response 
                return user 

            # authenticating the user
            auth_user = chk_password(request=request, user=user, password=data['password'] )
            ok_got_back(view='InstanceData.chk_password()', obj=auth_user)

            # ok response for authenticated user or an error response.
            return auth_user
        
        # handle any exceptions that occur during processing this method
        except Exception as e:
            return error_500(e=e, model='AnonymousFacade.login()')
        
        
    # method for register a new customer  
    def add_customer(self, request):
        ok_move_to(model='AnonymousFacade', func='add_customer()')
        
        try:
            # create new user
            new_user = self.create_new_user(request=request, user_role=3)
            ok_got_back(view='FacadeBase.create_new_user', obj=f'data {new_user}')      
            
            # check if no errors returned (FALSE)
            if validator.if_isinstance(new_user) != False:
                
                # error response 
                return new_user
            
            # got no errors, user successfully created 
            ok_chek_error_is_false(model='AnonymousFacade.add_customer()')
            
            # get the user_id from new user that been created
            user_id = new_user.user_id
            
            # validating the customer data with new user_id
            data = instance_data.customer_data(request=request, user_id=user_id)
            ok_got_back(view='instance_data.customer_data', obj=f'data {data}')               
            
            # check if no errors returned (FALSE)
            if validator.if_isinstance(data) != False:

                # if error, delete created user and return error response
                return user_delete(obj=data, obj_name='new_customer', user_id=user_id)  

            # got FALSE (no errors)
            ok_vlidate_data(model='FacadeBase', func='create_new_user')                   
            
            try:               
                # create new customer
                new_customer = api_Create_new(data=data, instance_model=Customers, model_serializer=CustomersSerializer)
                ok_got_back(view='SysApiViews', obj='new_customer')
                
                # check if no errors returned (FALSE)
                if validator.if_isinstance(new_customer) != False:
                    
                    # if error, delete created user and return error response
                    return user_delete(obj=new_customer, obj_name='new_customer', user_id=user_id)
                
                # got FALSE (no errors)                
                # serializering the data for the response (unique response for register process)
                new_customer_details = serialize_data(model_serializer=CustomersSerializer, instance_model=Customers, objects=new_customer, many=False)
                ok_got_back(view='operation_funcs', obj=new_customer_details)
                
                # login the new customer
                self.login(request=request)
                
                token = request.session['token']
                # successful register response with new customer details
                return ok_auth(user=token)
             
            # handle any exceptions that occur during creating the new customer or at data serializeing or at new user deleting        
            except Exception:
                return user_delete(obj=new_customer, obj_name='new_customer', user_id=user_id)
            
        # handle any exceptions that occur during processing this method  
        except Exception as e:
            return error_500(e=e, model='AnonymousFacade.add_customer()')