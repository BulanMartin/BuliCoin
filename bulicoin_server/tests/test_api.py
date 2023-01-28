from flask import Flask
import json


def test_complexity(client):
    response = client.get("/")

    #assert response.status_code == 404
    assert b"{\"Current number of leading zeros \": 4}" in response.data

'''
def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello, World!'
    assert response.status_code == 200

'''