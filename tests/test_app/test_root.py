# project/test_basic.py


import os
import unittest
from unittest import mock

from core import app, db


TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['BASEDIR'] = os.path.abspath(os.path.dirname(__file__))

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_DB

        """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        """
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass


    def test_index_page(self):
        index_page = self.app.get("/")
        html = index_page.data.decode()

        assert " Welcome to Shortify" in html
        assert index_page.status_code == 200

    @mock.patch('core.routes.generate_short_id')
    def test_user_can_shorten_url(self, mock):

        mock.return_value = "qwertyuio"
        
        payload = {
            "url": "https://github.com/culturemesh/culturemeshFFB", 
            "custom_id": ""
            }

        response = self.app.post("/", data= payload)
        html = response.data.decode()

        assert "qwertyuio" in html
        assert response.status_code == 200

    

if __name__ == "__main__":
    unittest.main()
