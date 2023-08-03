class InstanceData():

    def ticket_data(self, request):
        ticket_data = request.data
        flight_id = ticket_data.get('flight_id')
        cust_id = ticket_data.get('cust_id')
        return {
            'flight_id_id': flight_id, 
            'cust_id_id': cust_id
            }
    
    def airline_data(self, request):
            airline_data = request.data
            air_line_name = airline_data.get('air_line_name')
            airline_logo = airline_data.get('company_logo')
            country_id = airline_data.get('country_id')
            user_id = airline_data.get('user_id')
            return {'air_line_name': air_line_name, 
                    'company_logo': airline_logo, 
                    'country_id_id': country_id, 
                    'user_id_id': user_id 
                    }

    def flight_data(self, request):
            flight_data = request.data
            departure_time = flight_data.get('departure_time')
            landing_time = flight_data.get('landing_time')
            remaining_tickects = flight_data.get('remaining_tickects')
            air_line_id = flight_data.get('air_line_id')
            origin_country_id = flight_data.get('origin_country_id')
            destination_country_id = flight_data.get('destination_country_id')
            return {'departure_time': departure_time, 
                    'landing_time': landing_time, 
                    'remaining_tickects':remaining_tickects,
                    'air_line_id_id':air_line_id, 
                    'origin_country_id_id':origin_country_id, 
                    'destination_country_id_id':destination_country_id    
                    }