import unittest
from app import app
from test_helpers import response_success
import test_helpers
 
class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
    # executed after each test
    def tearDown(self):
        pass
    
    def test_success_route_one(self):
        response = self.app.get('/api/search?q=cam', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_success_route_two(self):
        response = self.app.get('/api/item/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_success_route_three(self):
        response = self.app.get('/api/search?q=cam', follow_redirects=True)
        self.assertEqual(response.data, b'{"items":[{"brand":"Panasonic","city":{"id":3,"name":"bogota"},"id":61,"name":"camara","price":369000.0,"rating":25.0,"thumbnail":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.sony.com.co%2Felectronics%2Fcamaras-lentes-intercambiables%2Filce-6000-body-kit&psig=AOvVaw3VXx6W5wSMtEYo7g6Cm_PT&ust=1632672777430000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKj6kJrCmvMCFQAAAAAdAAAAABAK"}],"query":"cam","seller":{"id":1,"logo":"https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg","name":"flask"},"total":1}\n')
    
    def success(self):
        print("gkjh")
        response = self.app.get('/api/search?q=cam', follow_redirects=True)
        assert test_helpers.response_success(response,response.status_code)

if __name__ == "__main__":
    unittest.main()
