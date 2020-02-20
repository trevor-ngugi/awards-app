from django.test import TestCase
from .models import Profile,Projects,ratings,User

# Create your tests here.
class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user= User(first_name="trevor", last_name='ngugi',username="t.ngugi", email="ngugi@gmail.com",)
        self.user.save()

        self.trevor= Profile(user=self.user, bio='web developer',no_of_projects=0, contact="07105191117",)
               
    def test_instance(self):
        self.assertTrue(isinstance(self.trevor,Profile))
    
    def test_save_method(self):
        self.trevor.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.trevor.save_profile()
        my_obj = Profile.objects.get(user=1)
        my_obj.delete()

class ProjectTestClass(TestCase):
    def setup(self):
        self.user= User(first_name="trevor", last_name='ngugi',username="t.ngugi", email="ngugi@gmail.com",)
        self.user.save()

        self.trevor= Profile(user=self.user, bio='web developer',no_of_projects=0, contact="07105191117",)
        self.trevor.trevor()

        self.project=Projects(title='akan-name',description='web application',link='testlink',name=self.trevor)

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Projects))