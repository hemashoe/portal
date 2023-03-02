from django.test import TestCase
from .models import User

class SignInTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test',
                                             password='test')
        self.user.save9