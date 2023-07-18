from django.urls import path
from .views import urlViews

app_name ='flghts_order_system'
urlpatterns = [
        path(
            'flights', 
            urlViews.flights, 
            name='flights'
            ),
        path(
            'flight_by_id/<int:flight_id>', 
            urlViews.get_flight_by_id, 
            name='flight_by_id'
            ),
        path(
            'get_flight_by_origin_country_id/<int:origin_country_id>', 
            urlViews.get_flight_by_origin_country_id, 
            name='get_flight_by_origin_country_id'
            ),
        path(
            'get_flight_by_destination_country_id/<int:destination_country_id>', 
            urlViews.get_flight_by_destination_country_id, 
            name='get_flight_by_destination_country_id'
            ),
        path(
            'get_flights_by_date/<str:departure_date>', 
            urlViews.get_flights_by_date, 
            name='get_flights_by_date'
            ),
        path(
            'get_flights_by_air_line_id/<int:air_line_id>', 
            urlViews.get_flights_by_air_line_id, 
            name='get_flights_by_air_line_id'
            ),
        path(
            'get_arrival_flights_by_country_id/<int:destination_country_id>', 
            urlViews.get_arrival_flights_by_country_id, 
            name='get_arrival_flights_by_country_id'
            ),
        path(
            'get_departure_flights_by_country_id/<int:origin_country_id>', 
            urlViews.get_departure_flights_by_country_id, 
            name='get_departure_flights_by_country_id'
            ),
        path(
            'airlines/', 
            urlViews.airlines, 
            name='airlines'
            ),
        path(
            'airline_by_id/<int:airline_id>', 
            urlViews.get_airline_by_id, 
            name='airline_by_id'
            ),
        path(
            'get_airline_by_country_id/<int:country_id>', 
            urlViews.get_airline_by_country_id, 
            name='get_airline_by_country_id'
            ),
        path(
            'countries/', 
            urlViews.countries, 
            name='countries'
            ),
        path(
            'country_by_id/<int:country_id>', 
            urlViews.get_country_by_id, 
            name='country_by_id'
            ),
        path(
            'create_new_user/', 
            urlViews.create_new_user, 
            name='create_new_user'
            ),
        path(
            'airline/<int:id>', 
            urlViews.airline, 
            name='airline'
            ),
        path(
            'get_my_flights_air_line_id/<int:air_line_id>', 
            urlViews.get_my_flights_air_line_id, 
            name='get_my_flights_air_line_id'
            ),
        path(
            'flight/<int:flight_id>', 
            urlViews.flight, 
            name='flight'
            ),
        path(
            'customer/<int:customer_id>', 
            urlViews.customer, 
            name='customer'
            ),
        path(
            'customers/', 
            urlViews.customers, 
            name='customers'
            ),
        path(
            'tickets/', 
            urlViews.tickets, 
            name='tickets'
            ),
        path(
            'ticket/<int:ticket_id>', 
            urlViews.ticket, 
            name='ticket'
            ),
        path(
            'get_my_tickets/<int:cust_id>', 
            urlViews.get_my_tickets, 
            name='get_my_tickets'
            ),
        path(
            'administrators/', 
            urlViews.administrators, 
            name='administrators'
            ),
        path(
            'administrator/<int:admin_id>', 
            urlViews.administrator, 
            name='administrator'
            ),
















        path(
            'get_airline_by_username/<str:username>', 
            urlViews.get_airline_by_username, 
            name='get_airline_by_username'
            ),
        path('get_customer_by_username/<str:username>', urlViews.get_customer_by_username, name='get_customer_by_username'),
        path('get_user_by_username/<str:username>', urlViews.get_user_by_username, name='get_user_by_username'),
        
        #path('get_flight_by_air_line_id/<int:air_line_id>', urlViews.get_flight_by_air_line_id, name='get_flight_by_air_line_id'),
        
        #path('get_arrival_flights_by_country_id/<int:destination_country_id>', urlViews.get_arrival_flights_by_country_id, name='get_arrival_flights_by_country_id'),
        path('', urlViews.index, name='index'),
        
        
        #path('countries/', urlViews.countries, name='countries'),
        
        



        path('addUserRoleHttpForm/', urlViews.addUserRoleHttpForm, name='addUserRoleHttpForm'),
       
        path('addMultiUserRoles/', urlViews.add_multi_user_roles, name='add_multi_user_roles'),
        path('userRole/', urlViews.user_role, name='user_role'),

]