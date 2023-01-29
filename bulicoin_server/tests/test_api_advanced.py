from flask import Flask
import json

# Check api functions combined with mining
def test_mining(client):
    response = client.get("/get_chain")

    assert response.status_code == 200
    assert b"{\"chain\":[{\"current_complexity\":4,\"index\":1,\"nonce\":1,\"prev_hash\":\"0\",\"timestamp\":\"" in response.data
    assert b"\",\"transactions\":[]}],\"length\":1}\n" in response.data

    client.get("/mine_block")
    client.get("/mine_block")

    # check that chain length is 3
    response = client.get("/get_chain")
    assert b"\"length\":3" in response.data

    response = client.get("/validate")

    assert response.status_code == 200
    assert b"{\"Chain valid\":true}\n" in response.data