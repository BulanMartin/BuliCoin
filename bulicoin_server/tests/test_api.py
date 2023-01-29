from flask import Flask
import json

# Check that index page is rendered
def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"<h1>Welcome to BuliCoin node</h1>" in response.data

# Check reading out and setting the complexity (number of leading zeros) value
def test_complexity(client):
    response = client.get("/complexity/")
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response['Current number of leading zeros ']==4

    response = client.get("/complexity/2")
    json_response = response.get_json()
    assert response.status_code == 200
    assert json_response['Leading zeros set to ']==2

    response = client.get("/complexity/")
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response['Current number of leading zeros ']==2

# Check that block is mined
def test_mining(client):
    response = client.get("/mine_block")
    json_response = response.get_json()

    assert response.status_code == 200

    assert json_response['Blockchain']=='New block was mined!'
    assert json_response['current_complexity']==4
    assert json_response['index']==2
    assert isinstance(json_response['nonce'], int)
    assert isinstance(json_response['previous_hash'], str)
    assert len(json_response['previous_hash']) == 64
    assert json_response['previous_hash'][:4]=='0000'
    assert isinstance(json_response['timestamp'], str)
    assert len(json_response['timestamp']) == 26
    assert len(json_response['transactions']) == 1
    assert json_response['transactions'][0]['amount']==1
    assert isinstance(json_response['transactions'][0]['receiver'], str)
    assert len(json_response['transactions'][0]['receiver'])==32
    assert json_response['transactions'][0]['sender']=='BuliCoin network'

# Check that chain with initial block is returned
def test_get_chain(client):
    response = client.get("/get_chain")
    json_response = response.get_json()

    assert response.status_code == 200

    assert json_response['chain'][0]['current_complexity']==4
    assert json_response['chain'][0]['index']==1
    assert json_response['chain'][0]['nonce']==1
    assert json_response['chain'][0]['prev_hash']=='0'
    assert len(json_response['chain'][0]['timestamp']) > 0
    assert len(json_response['chain'][0]['transactions']) == 0
    assert json_response['length'] == 1


# Check validity response on blockchain with only initial block is True
def test_validation(client):

    response = client.get("/validate")
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response['Chain valid']==True