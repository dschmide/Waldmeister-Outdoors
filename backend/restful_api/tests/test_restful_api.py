from django.test import TestCase, Client


class Areas(TestCase):
    base_url = '/api/waldmeister-map'

    def test_area_get(self):
        # Create an instance of a GET request.
        c = Client()
        response = c.get(self.base_url + '/api/areas/')
        self.assertEqual(response.status_code, 200)

    def test_area_wrongdata_notloggedin(self):
        # Create an instance of a POST request.
        c = Client()
        response = c.post(self.base_url + '/api/areas/', {'username': 'testuser3'})  # noqa
        print(response.content)
        self.assertEqual(response.status_code, 401)

    def test_area_correct_notloggedin(self):
        # Create an instance of a POST request.
        c = Client()
        response = c.post(
            self.base_url + '/api/areas/',
            {
                "label": "testarea1",
                "public": True,
                "polygon": {
                    "type": "MultiPolygon", "coordinates": [[[
                        [47.44852243794931,8.744945526123049],[47.42530003183073,8.729152679443361],[47.416937456635445,8.770694732666017],[47.44852243794931,8.744945526123049]  # noqa
                    ]]]
                }
            }
        )
        print(response.content)
        self.assertEqual(response.status_code, 401)


class UserTests(TestCase):
    base_url = '/api/waldmeister-map'

    def test_auth_ok_nomail(self):
        # Create an instance of a POST request.
        c = Client()
        response = c.post(self.base_url + '/auth/users/create/', {'username': 'testuser', 'password': '1234ASDF'})  # noqa
        self.assertEqual(response.status_code, 201)

    def test_auth_badpw(self):
        # Create an instance of a POST request.
        c = Client()
        response = c.post(self.base_url + '/auth/users/create/', {'username': 'testuser2', 'password': 'asdf'})  # noqa
        self.assertEqual(response.status_code, 400)

    def test_auth_ok_withmail(self):
        # Create an instance of a POST request.
        c = Client()
        response = c.post(
            self.base_url + '/auth/users/create/',
            {'username': 'testuser3', 'password': '1234ASDF', 'email': 'asdfghj@gmail.com'}  # noqa
        )
        self.assertEqual(response.status_code, 201)

    def test_auth_ok_badmail(self):
        # Create an instance of a POST request.
        c = Client()
        response = c.post(
            self.base_url + '/auth/users/create/', {'username': 'testuser3', 'password': '1234ASDF', 'email': 'asdfgh'}  # noqa
        )
        self.assertEqual(response.status_code, 400)

    def test_login_correct(self):
        # Create an instance of a POST request.
        c = Client()
        # Create a User
        response = c.post(
            self.base_url + '/auth/users/create/',
            {'username': 'testuser3', 'password': '1234ASDF', 'email': 'asdfghj@gmail.com'}  # noqa
        )
        # Login with the same User, get a token
        response = c.post(
            self.base_url + '/auth/jwt/create/', {'username': 'testuser3', 'password': '1234ASDF'}  # noqa
        )
        print("token: ")
        print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_login_correct_post_area(self):
        # Create an instance of a POST request.
        c = Client()
        # Create a User
        response = c.post(
            self.base_url + '/auth/users/create/',
            {'username': 'testuser3', 'password': '1234ASDF', 'email': 'asdfghj@gmail.com'}  # noqa
        )
        # Login with the same User, get a token
        response = c.post(
            self.base_url + '/auth/jwt/create/', {'username': 'testuser3', 'password': '1234ASDF'}  # noqa
        )
        print("token: ")
        # print(response.context_data)
        # print(response.context['token'])
        self.assertEqual(response.status_code, 200)
