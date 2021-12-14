from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
import datetime as dt


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user='georgez', bio='coolguy', profile_photo='cloudlink.cloud')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

class ProjectTestClass(TestCase):
    def setUp(self):
        self.project = Project(title='Nulla-quis', project_image='cloudlink.cloud', description='Fusce nec tellus sed augue semper porta', link='tess.com', pub_date='2021', prof_ref='georgezProfile')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))