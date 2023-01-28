from flask import Flask
import json

def test_complexity(client):
    response = client.get("/complexity/")

    assert response.status_code == 200
    assert b"{\"Current number of leading zeros \":4}\n" in response.data

