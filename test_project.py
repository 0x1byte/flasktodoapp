import pytest
from project import app

@pytest.fixture
def client():
    # app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_add_todo(client):
    # Send a POST request to add a new todo
    response = client.post('/add', data={'todo': 'Test Todo'})

    # Check if the response is a redirect to the index page
    assert response.status_code == 302

    # Send a GET request to the index page to check if the todo is added
    response = client.get('/')
    assert b'Test Todo' in response.data

def test_update_todo(client):
    # Send a POST request to update a todo
    response = client.post('/update/1', data={'todo': 'Updated Todo'})

    # Check if the response is a redirect to the index page
    assert response.status_code == 302

    # Send a GET request to the index page to check if the todo is updated
    response = client.get('/')
    assert b'Updated Todo' in response.data
