from django.test import TestCase, Client

# Create your tests here.
class Areas(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        #self.user = User.objects.create_user(
        #    username='jacob', email='jacob@…', password='top_secret')
        pass

    def test_area_get(self):
        # Create an instance of a GET request.
        c = Client()
        response = c.get('/WaldmeisterMap/api/areas/')
        self.assertEqual(response.status_code, 200)
