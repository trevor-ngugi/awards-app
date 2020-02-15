from django.test import TestCase
from .models import Profile,Projects,ratings

# Create your tests here.
class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.trevor= Profile(name="trevor", bio='web developer',no_of_projects=0, contact="07105191117",)
       

        
    def test_instance(self):
        self.assertTrue(isinstance(self.trevor,Profile))
