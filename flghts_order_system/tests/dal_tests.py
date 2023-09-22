import unittest
from django.test import RequestFactory
from ..dal.dalViews import Dal
from ..dal.models import Users, Customers, AirLineCompanies, UserRole


class TestDalTableObjectsList(unittest.TestCase):
    def setUp(self):
        # Set up test environment
        self.factory = RequestFactory()  # Create a RequestFactory instance
        self.dal_instance = Dal()  # Instantiate the Dal class
        self.dal_instance.model = Users  # Specify the model for testing
        user_role = UserRole.objects.create(role_name='testAdministrator5') 
        # Create sample objects for testing
        self.sample_object1 = Users.objects.create(user_name='Avnerico', password='abc123', email='avner@mail.com', user_role=user_role)
        #self.sample_object2 = Customers.objects.create()
        # ... create more sample objects if needed

        # create UserRole instance
         

    def tearDown(self):
        # Clean up after each test
        self.sample_object1.delete()
        #self.sample_object2.delete()
        # ... delete other sample objects if created

    def test_table_objects_list(self):
        # Test the table_objects_list method
        
        # Create a mock GET request
        request = self.factory.get('/http://127.0.0.1:8000/flight_tick_order_sys/flights/') 
        
        # Call the table_objects_list method and pass the model
        response = self.dal_instance.table_objects_list(self.dal_instance.model)

        # Check the response status code (should be 200 for success)
        #self.assertEqual(response., 200)
        
        # Check if the created sample objects are present in the response data
        self.assertIn(self.sample_object1, response)
        #self.assertIn(self.sample_object2, response.data)
        # ... check other objects if created

if __name__ == '__main__':
    unittest.main()