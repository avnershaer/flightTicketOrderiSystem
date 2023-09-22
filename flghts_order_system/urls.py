from django.urls import path
from .views import urlViews

app_name ='flghts_order_system'
urlpatterns = [
        
        # authintication
        path('login/', urlViews.login, name='login'),
        path('logout/', urlViews.logout, name='logout'), #!
        
        # flights
        path('flights/', urlViews.flights, name='flights'),#!
        path('flight/<int:flight_id>/', urlViews.flight, name='flight'),#!
        path('get_flights_by_origin_country_id/<int:origin_country_id>/', urlViews.get_flights_by_origin_country_id, name='get_flight_by_origin_country_id'),#!
        path('get_flights_by_destination_country_id/<int:destination_country_id>/', urlViews.get_flights_by_destination_country_id, name='get_flights_by_destination_country_id'),#!
        path('get_flights_by_departure_date/<str:departure_date>/', urlViews.get_flights_by_departure_date, name='get_flights_by_departure_date'),#!
        path('get_flights_by_landing_date/<str:landing_date>/', urlViews.get_flights_by_landing_date, name='get_flights_by_landing_date'),#!
        path('get_flights_by_air_line_id/<int:air_line_id>/', urlViews.get_flights_by_air_line_id, name='get_flights_by_air_line_id'),#!
        path('get_arrival_flights_by_country_id/<int:destination_country_id>/', urlViews.get_arrival_flights_by_country_id, name='get_arrival_flights_by_country_id'),#!
        path('get_departure_flights_by_country_id/<int:origin_country_id>/', urlViews.get_departure_flights_by_country_id, name='get_departure_flights_by_country_id'),#!
        path('get_my_flights/', urlViews.get_my_flights, name='get_my_flights'),#!
        path('add_flight/', urlViews.add_flight, name='add_flight'),#!
        path('update_flight/<int:flight_id>/', urlViews.update_flight, name='update_flight'),#!
        path('remove_flight/<int:flight_id>/', urlViews.remove_flight, name='remove_flight'),#!

        # airlines
        path('airlines/', urlViews.airlines, name='airlines'),#!
        path('airline_by_id/<int:airline_id>/', urlViews.get_airline_by_id, name='airline_by_id'),
        path('get_airline_by_country_id/<int:country_id>/', urlViews.get_airline_by_country_id, name='get_airline_by_country_id' ),#!
        path('airline/<int:air_line_id>/', urlViews.airline, name='airline'),#!
        path('add_airline/', urlViews.add_airline, name='add_airline'),#!
        path('remove_airline/<int:air_line_user_id>/', urlViews.remove_airline, name='remove_airline'),#!
        path('air_line_by_user_id/<int:user_id>/', urlViews.air_line_by_user_id, name='air_line_by_user_id'),#!

        # countries
        path('countries/', urlViews.countries, name='countries'),#!
        path('country_by_id/<int:country_id>/', urlViews.get_country_by_id, name='country_by_id'),#!

        #customer
        path('add_customer/', urlViews.add_customer, name='add_customer'),#!
        path('customer/<int:customer_id>/', urlViews.customer, name='customer'),#!
        path('remove_customer/<int:customer_id_user_id>/', urlViews.remove_customer, name='remove_customer'),#!
        path('customers/', urlViews.customers, name='customers'),#!
        path('customer_by_user_id/<int:user_id>/', urlViews.customer_by_user_id, name='customer_by_user_id'),#!

        # tickets
        path('tickets/', urlViews.tickets, name='tickets'),#!
        path('ticket/<int:ticket_id>', urlViews.ticket, name='ticket'),#!
        path('get_my_tickets/', urlViews.get_my_tickets, name='get_my_tickets'),#!
        path('get_all_tickets/', urlViews.get_all_tickets, name='get_all_tickets'),#!

        # administrator    
        path('administrators/', urlViews.administrators, name='administrators'),#!
        path('administrator/<int:admin_id>/', urlViews.administrator, name='administrator'),#!
        path('remove_administrator/<int:admin_id>/', urlViews.remove_administrator, name='remove_administrator'),#!
        path('admin_by_user_id/<int:user_id>/', urlViews.admin_by_user_id, name='admin_by_user_id'),#!
        path('administrators_list/', urlViews.administrators_list, name='administrators_list'),#!

]