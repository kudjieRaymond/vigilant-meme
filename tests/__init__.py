import pytest
import os
import tempfile

from core import app
#from decouple import config
import config


@pytest.fixture
def client():

    app.config.from_object(config.TestingConfig)
    #client = app.test_client()

    #yield client

    with app.test_client() as client:
        yield client
        
    # db_fd, db_path = tempfile.mkstemp()
    # app.config.from_object(config.TestingConfig)
    # #app = create_app({'TESTING': True, 'DATABASE': db_path})

    # with app.test_client() as client:
    #     with app.app_context():
    #         init_db()
    #     yield client

    # os.close(db_fd)
    # os.unlink(db_path)
