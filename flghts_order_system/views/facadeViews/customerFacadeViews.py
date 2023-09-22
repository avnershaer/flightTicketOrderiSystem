from .anonimousFacadeViews import AnonymousFacade
from ...api.SysApiViews import *


validator = GetValidations()
instance_data = InstanceData()


class CustomerFacade(AnonymousFacade):

    # customer role (3) login require
    @require_role(1,3)
    def customer_details_by_user_id(self, request, user_id):
        ok_move_to(model='CustomerFacade', func='customer_details_by_user_id')
        logger.info(f'request:{request}') 
        logger.info(f'user_id:{user_id}') 
        try:
             customer = api_get_object_by_user_id(model=Customers, user_id=user_id, model_serializer=CustomersSerializer)
             ok_got_back(view='api_get_object_by_user_id', obj=customer)
             logger.info(f'success retrieveing customer :{customer} - HTTP/1.1 200 OK')
             # returns the airline_id
             return customer
         
         # if getting airline fails, return 403 error
        except:
             return error_403()
    
    # customer role (3) login require
    @require_role(3) 
    # method for update customer
    def update_customer(self, request, customer_id):
        ok_move_to(model='CustomerFacade', func='update_customer()')
        
        try:
            # authenticate customer for updating self details
            auth_update = validator.valid_user_for_operation(request=request, model=Customers, model1=Customers, attr_name='cust_id', id=customer_id, attr_name2='cust_id', operation='UPDATE THIS CUSTOMER')
            ok_got_back(view='validatorsView', obj=f'auth for delete:{auth_update}')
            
            # customer is not authenticate for updating details
            if auth_update != True:
                
                # error response
                return auth_update
            
            # get the user_id from token dictionary
            cust_user_id = request.session.get('token')['id']  
            logger.info(f'OK got cust_token_user_id: {cust_user_id} - HTTP/1.1 200 OK')
            
            #validating the new customer data
            valid_cust_data = instance_data.customer_data(request=request, user_id=cust_user_id)
            ok_got_back(view='operations_classes', obj='valid_cust_data()')

            # check if no errors returned (FALSE)
            if validator.if_isinstance(valid_cust_data) != False:
                
                # error response
                return valid_cust_data
            
            # take out the user_id from data before updating the instance
            valid_cust_data.pop('user_id_id', None)
            
            # update customer details
            updated_customer = api_update_instance(validated_data=valid_cust_data, id=customer_id,instance_model=Customers, model_serializer=CustomersSerializer)
            ok_got_back(view='SysApiViews', obj='updated_customer')
            
            # success response with updated details or an error response.
            return updated_customer

        # handle any exceptions that occur during processing this method  
        except Exception as e: 
                return error_500(e=e, model='CustomerFacadeViews.update_customer()') 

    
    # customer role (3) login require
    @require_role(3)
    # mothod for ticket ordering 
    def add_ticket(self, request):
        ok_move_to(model='CustomerFacade', func='add_ticket')

        try:
            # get the user_id from token dictionary
            cust_user_id = request.session.get('token')['id']  
            logger.info(f'OK got cust_token_user_id: {cust_user_id} HTTP/1.1 200 OK')

            # get cust_id by the user_id
            cust_id = get_cust_id_by_user_id(request=request)

            # check if got cust_id (False)       
            if validator.if_isinstance(cust_id) != False:

                # error response
                return cust_id 

            # get data for the ticket from request
            data = instance_data.ticket_data(request=request, cust_id=cust_id)
            ok_got_back(view='instance_data', obj=f'data {data}')

            # check if no errors on data (False)
            if validator.if_isinstance(data) != False:

                # error response
                return data

            try:
                # add the new ticket for the customer            
                new_ticket = api_Create_new(data=data, instance_model=Tickets, model_serializer=TicketsSerializer)
                ok_got_back(view='SysApiViews', obj='new_ticket')

                # success reponse with ticket and flight details or an error response.  
                return new_ticket

            # handle any exceptions that occur during adding the ticket 
            except Exception as e:
                return error_500(e=e, model='CustomerFacadeViews.add_ticket()')
        
        # handle any exceptions that occur during processing this method 
        except Exception as e:
                return error_500(e=e, model='CustomerFacadeViews.add_ticket()')
        
    
    # customer role (3) login require
    @require_role(3) 
    # method for delete ticket
    def remove_ticket(self, request, ticket_id):
        ok_move_to(model='CustomerFacade', func='remove_ticket')
        
        try:
            # authenticate customer for removing his self ticket
            auth_delete = validator.valid_user_for_operation(request=request, model=Customers, model1=Tickets, attr_name='ticket_id', id=ticket_id, attr_name2='cust_id', operation='REMOVE THIS TICKET')
            ok_got_back(view='validatorsView', obj=f'auth for delete:{auth_delete}')
            
            # customer is not authenticate for updating details
            if auth_delete != True:
                
                # error response
                return auth_delete

            try:
                #delete ticket
                ticket_for_delete = api_delete(id=ticket_id, instance_model=Tickets)
                ok_got_back(view='SysApiViews', obj='ticket_for_delete')
                
                # success reponse with delted ticket id or an error response.  
                return ticket_for_delete
            
            # handle any exceptions that occur during ticket deleting
            except Exception as e:
                return error_500(e=e, model='CustomerFacade.remove_ticket()')
           
        # handle any exceptions that occur during processing this method         
        except Exception as e:
            return error_500(e=e, model='CustomerFacade.remove_ticket()')


    # customer role (3) login require
    @require_role(3)
    # mothod for get customers tickets
    def get_my_tickets(self, request):
        ok_move_to(model='CustomerFacade', func='get_my_tickets')     
        
        try:
            # get the customer id by the user_id from token
            cust_id = get_cust_id_by_user_id(request=request)
            ok_got_back(view='get_cust_id_by_user_id', obj=cust_id)
            
            # check if cust_id is available in the session (False)
            if validator.if_isinstance(cust_id) != False:

                # error response
                return cust_id
             
            try:
                # get customer tickets details list
                my_tickets = api_get_object_by_entity_id(id=cust_id, instance_model=Tickets, model_serializer=TicketsSerializer, entity='cust_id')
                ok_got_back(view='SysApiViews', obj='my_tickets')
                
                # success reponse with tickets details list or an error response. 
                return my_tickets
            
            # handle any exceptions that occur during getting customer tickets list
            except Exception as e:
               return error_500(e=e, model='CustomerFacade')
     
        # handle any exceptions that occur during processing this method    
        except Exception as e:
            return error_500(e=e, model='CustomerFacade.get_my_tickets().')