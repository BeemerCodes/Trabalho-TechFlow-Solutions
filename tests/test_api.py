import pytest
from src.app import app, db, Task

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_task_success(client):
    response = client.post('/tasks', json={'title': 'Configurar servidor'})
    assert response.status_code == 201
    assert response.get_json()['title'] == 'Configurar servidor'

def test_create_task_missing_title(client):
    response = client.post('/tasks', json={'status': 'Em Progresso'})
    assert response.status_code == 400

def test_list_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)