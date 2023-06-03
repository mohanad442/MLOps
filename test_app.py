from fastapi.testclient import TestClient
from app import app 

client = TestClient(app)

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.content == b'"OK"'
    
def test_predict():
    response = client.post('/predict', json = {'a': 2, 'b': 'Hello', 'c': [1,2,3,4]})
    assert response.status_code == 200
    assert response.json() ==  3