from .anonimousFacadeViews import AnonymousFacade
from .facadeBaseViews import FacadeBase
from ...api.SysApiViews import *


class AdministratorFacade(AnonymousFacade):
    
    @require_role(1)
    def admin_details_by_user_id(self, request, user_id):
        ok_move_to(model='AdministratorFacade', func='admin_details_by_user_id')
        logger.info(f'request:{request}') 
        logger.info(f'user_id:{user_id}') 
        try:
             # retrieve admin that associated with user_id
             admin = api_get_object_by_user_id(model=Adminstrators, user_id=user_id, model_serializer=AdministratorSerializer)
             ok_got_back(view='api_get_object_by_user_id', obj=admin)
             logger.info(f'success retrieveing admin :{admin} - HTTP/1.1 200 OK')
             # returns the airline_id
             return admin
         
         # if getting admin fails, return 403 error
        except:
             return error_403()
  
    # administrator role (1) login require
    @require_role(1)
    # method for getting list of all customers in system
    def get_all_customers(self, request): #(request for @require_role)
        ok_move_to(model='AdministratorFacade', func='get_all_customers()')
        
        try:
            # get list of all customers details
            customers_list = api_get_list(instance_model=Customers, model_serializer = CustomersSerializer)
            ok_got_back(view='SysApiViews', obj='customers_list')
            
            # success reponse with list of all customers details or an error response.  
            return customers_list 
        
        # handle any exceptions that occur during getting customers list 
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')

    # administrator role (1) login require
    @require_role(1)
    # method for registering new airline
    def add_airline(self, request):
        ok_move_to(model='AdministratorFacade', func='add_airline()')
        
        try:
            # create new user
            new_user = self.create_new_user(request=request, user_role=2)
            ok_got_back(view='create_new_user', obj=f'data {new_user}')
            
            # check if no errors returned (FALSE)
            if validator.if_isinstance(new_user) != False:
                
                # error response 
                return new_user

            # got no errors, user successfully created 
            ok_chek_error_is_false(model='AdministratorFacade.add_airline()')
            
            # get the user_id from new user that been created
            user_id = new_user.user_id
            
            # validating the customer data with new user_id
            data = instance_data.airline_data(request=request, user_id=user_id)
            ok_got_back(view='instance_data.airline_data', obj=f'data: {data}')
            
            # check if no errors returned (FALSE)
            if validator.if_isinstance(data) != False:
                
                # if error, delete created user and return error response
                return user_delete(obj=data, obj_name='new_airline', user_id=user_id)   

            # got FALSE (no errors)
            ok_vlidate_data(model='FacadeBase', func='create_new_user')   
            
            try:
                # create new airline
                new_airline = api_Create_new(data=data, instance_model=AirLineCompanies, model_serializer=AirlineSerializer)
                ok_got_back(view='SysApiViews', obj='new_airline')
                
                # check if no errors returned (FALSE)
                if validator.if_isinstance(new_airline) != False:
                    
                    # if error, delete created user and return error response
                    return user_delete(obj=new_airline, obj_name='new_airline', user_id=user_id) 
                
                # got FALSE (no errors)
                # serializering the data for the response (unique response for register process)
                ok_chek_error_is_false(model='AnonymousFacade.add_customer()')
                new_airline_details = serialize_data(model_serializer=AirlineSerializer, instance_model=AirLineCompanies, objects=new_airline, many=False)
                ok_got_back(view='operation_funcs', obj=new_airline_details)
                
                # successful register response with new airline details
                return new_airline_details

            # handle any exceptions that occur during creating the new airline or at data serializeing or at new user deleting        
            except Exception as e:
                return error_500(e=e, model='AdministratorFacade.add_airline()')
           
        # handle any exceptions that occur during processing this method  
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade.add_airline()')


    # administrator role (1) login require
    @require_role(1)
    # method for registering new airline
    def add_administrator(self, request):
        ok_move_to(model='AdministratorFacade', func='add_administrator')
        
        try:
            # create new user
            new_user = self.create_new_user(request=request, user_role=1)
            ok_got_back(view='facadeBase.create_new_user', obj=f'data {new_user}')
            
             # check if no errors returned (FALSE)
            if validator.if_isinstance(new_user) != False:
                
                # error response 
                return new_user  

            # got no errors, user successfully created 
            ok_chek_error_is_false(model='AdministratorFacade.add_administrator()')
            
            # get the user_id from new user that been created
            user_id = new_user.user_id
            
            # validating the administrator data with new user_id
            data = instance_data.administrator_data(request=request, user_id=user_id)
            ok_got_back(view='instance_data', obj=f'data {data}')
            
            # check if no errors returned (FALSE)
            if validator.if_isinstance(data) != False:

                # if error, delete created user and return error response
                return user_delete(obj=data, obj_name='new_administrator', user_id=user_id)
            
            # got FALSE (no errors)
            ok_vlidate_data(model='AdministratorFacade', func='add_administrator')
            
            try:
                # create new administrator
                new_administrator = api_Create_new(data = data, instance_model=Adminstrators, model_serializer=AdministratorSerializer)
                ok_got_back(view='SysApiViews', obj='new_administrator')
                
                # check if no errors returned (FALSE)
                if validator.if_isinstance(new_administrator) != False:
                    
                    # if error, delete created user and return error response
                    return user_delete(obj=new_administrator, obj_name='new_administrator', user_id=user_id)
                
                # got FALSE (no errors)
                # serializering the data for the response (unique response for register process)
                new_administrator_details = serialize_data(model_serializer = AdministratorSerializer, instance_model = Adminstrators, objects=new_administrator, many=False)
                ok_got_back(view='operation_funcs', obj=new_administrator_details)
                
                # successful register response with new airline details
                return new_administrator_details
                
            # handle any exceptions that occur during creating the new airline or at data serializeing or at new user deleting              
            except Exception as e:
                return error_500(e=e, model='AdministratorFacade.add_administrator()')   
                
        # handle any exceptions that occur during processing this method    
        except Exception as e:
            return error_500(e=e, model='AnonymousFacade.add_administrator()')


    # administrator role (1) login require       
    @require_role(1)
    # method for updating administrator details
    def update_administrator(self, request, admin_id):
        ok_move_to(model='AdministratorFacade', func='update_administrator()')
        
        try:
            # authenticate airline for updating self details
            auth_update = validator.valid_user_for_operation(request=request, model=Adminstrators, model1=Adminstrators, attr_name='admin_id', id=admin_id, attr_name2='admin_id', operation='UPDATE THIS ADMINISTRATOR')
            ok_got_back(view='validatorsView', obj=f'auth for delete:{auth_update}')

            # administrator is not authenticate for updating details
            if auth_update != True:
                
                # error response
                return auth_update
            
            # get user_id from token dictionary    
            admin_user_id = request.session.get('token')['id']  
            logger.info(f'OK got admin_token_user_id: {admin_user_id} - HTTP/1.1 200 OK')
            
            # validating data for updating
            valid_admin_data = instance_data.administrator_data(request=request, user_id=admin_id)
            
            # if administrator data not valid 
            if validator.if_isinstance(valid_admin_data) != False:
                
                # error response
                return valid_admin_data


            # data is valid
            # take out user_id fromdata before updating instance
            valid_admin_data.pop('user_id_id', None)
            
            try:
                # update administrator details
                updated_admin = api_update_instance(validated_data=valid_admin_data, id=admin_id, instance_model=Adminstrators, model_serializer=AdministratorSerializer)
                
                # success reponse with administrator new details or an error response.
                return updated_admin
            
            # handle any exceptions that occur during updating administrator details 
            except Exception as e:
                return error_500(e=e, model='AirLinesFacade.update_airline()')
        
        # handle any exceptions that occur during processing this method      
        except Exception as e: 
                return error_500(e=e, model='AdministratorFacade.update_administrator()') 


    # administrator role (1) login require
    @require_role(1)
    # method for deleting airline   
    def remove_airline(self, request, air_line_user_id):#(request for @require_role )
        ok_move_to(model='AdministratorFacade', func='remove_airline')  
        
        try:
            # deleting airline
            airline_for_delete = api_delete(id=air_line_user_id, instance_model=Users)
            ok_got_back(view='SysApiViews', obj='airline_for_delete')
            
            # success response with deleted airline_id or an error response.
            return airline_for_delete
        
        # handle any exceptions that occur during deleting flight 
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')   
    

    # administrator role (1) login require
    @require_role(1)
    # method for deleting customer  
    def remove_customer(self, request, customer_id_user_id):#(request for @require_role )
        ok_move_to(model='AdministratorFacade', func='remove_customer')
        
        try:
            # deleting airline
            customer_for_delete = api_delete(id=customer_id_user_id, instance_model=Users)
            ok_got_back(view='SysApiViews', obj='customer_for_delete')
            
            # success response with deleted cust_id or an error response.
            return customer_for_delete
        
        # handle any exceptions that occur during deleting customer 
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')
    

    # administrator role (1) login require
    @require_role(1)
    # method for deleting customer 
    def remove_administrator(self, request, admin_id): #(request for @require_role )
        ok_move_to(model='AdministratorFacade', func='remove_administrator')
        try:
            # deleting administrator
            administrator_for_delete = api_delete(id=admin_id, instance_model=Users)
            ok_got_back(view='SysApiViews', obj='administrator_for_delete')
            
            # success response with deleted admin_id or an error response.
            return administrator_for_delete
        
        # handle any exceptions that occur during deleting administrator 
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')


    # administrator role (1) login require
    @require_role(1)
    # method for getting list of all tickets in system
    def get_all_tickets(self, request):#(request for @require_role)
        ok_move_to(model='AdministratorFacade', func='get_all_tickets')
        
        try:
            # get list of all tickets details
            tickets_list = api_get_list(instance_model=Tickets, model_serializer = TicketsSerializer)
            ok_got_back(view='SysApiViews', obj='customers_list')
            
            # success reponse with list of all tickets details or an error response.  
            return tickets_list 
        
        # handle any exceptions that occur during getting tickets list 
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')

    # administrator role (1) login require
    @require_role(1)
    # method for getting list of all administrators in system 
    def get_all_administrators(self, request): #(request for @require_role)
        ok_move_to(model='AdministratorFacade', func='get_all_administrators()')
        
        try:
            # get list of all customers details
            administrators_list = api_get_list(instance_model=Adminstrators, model_serializer = AdministratorSerializer)
            ok_got_back(view='SysApiViews', obj='administrators_list')
            
            # success reponse with list of all administrators details or an error response.  
            return administrators_list 
        
        # handle any exceptions that occur during getting customers list 
        except Exception as e:
            return error_500(e=e, model='AdministratorFacade')