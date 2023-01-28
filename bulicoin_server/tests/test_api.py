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

    assert response.status_code == 200
    assert b"{\"Current number of leading zeros \":4}\n" in response.data

    response = client.get("/complexity/2")
    assert response.status_code == 200
    assert b"{\"Leading zeros set to \":2}\n" in response.data

    response = client.get("/complexity/")

    assert response.status_code == 200
    assert b"{\"Current number of leading zeros \":2}\n" in response.data

# Check that block is mined
def test_mining(client):
    response = client.get("/mine_block")

    assert response.status_code == 200
    assert b"New block was mined!" in response.data
    assert b"\"index\":2," in response.data
    assert b"\"sender\":\"BuliCoin network\"" in response.data

# Check that chain with initial block is returned
def test_mining(client):
    response = client.get("/get_chain")

    assert response.status_code == 200
    assert b"{\"chain\":[{\"current_complexity\":4,\"index\":1,\"nonce\":1,\"prev_hash\":\"0\",\"timestamp\":\"" in response.data
    assert b"\",\"transactions\":[]}],\"length\":1}\n" in response.data

# Check validity response on blockchain with only initial block is True
def test_index(client):

    response = client.get("/validate")

    assert response.status_code == 200
    assert b"{\"Chain valid\":true}\n" in response.data