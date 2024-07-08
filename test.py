import requests
def test_frontend():
    response = requests.get('http://localhost:8080')
    assert response.status_code == 200
    assert "Hello from backend" in response.text

if _name_ == "_main_":
    test_frontend()
    print("Test passed!")
