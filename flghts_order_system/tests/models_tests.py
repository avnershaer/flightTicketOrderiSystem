from django.test import TestCase, RequestFactory
from ..dal.models import Users, UserRole
from loggers.loggers import lggr
from ..dal.dalViews import Dal
import unittest


loggr = lggr()


class UsersModelTests(TestCase):

    def setUp(self):
        
        # create UserRole instance
        user_role = UserRole.objects.create(role_name='Administrator')  
        
        # create Users instance with the created UserRole instance
        self.user = Users(user_name='Avnerico', password='abc123', email='avner@mail.com', user_role=user_role)
        self.user.save()

    def test_username_text(self):
        
        # etrieve first user from the database    
        db_user = Users.objects.all().first()
        
        # compare username in the database with the expected username
        self.assertEqual(db_user.user_name, self.user.user_name)
        
        # Log the comparison result for debugging purposes
        loggr.info(f'db_user.user_name:{db_user.user_name}  = self.user.user_name: {self.user.user_name} ')

    def test_password_text(self):
        
        # etrieve first user from the database    
        db_user = Users.objects.all().first()
        
        # compare password in the database with the expected password
        self.assertEqual(db_user.password, self.user.password)
        
        # log the comparison result (for debugging purposes)
        loggr.info(f'db_user.password:{db_user.password}  = self.user.password: {self.user.password} ')



if __name__ == '__main__':
    unittest.main()