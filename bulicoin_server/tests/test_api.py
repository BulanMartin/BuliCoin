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
    assert response.json['Current number of leading zeros ']==4

    response = client.get("/complexity/2")

    assert response.status_code == 200
    assert response.json['Leading zeros set to ']==2

    response = client.get("/complexity/")

    assert response.status_code == 200
    assert response.json['Current number of leading zeros ']==2

# Check that block is mined
def test_mining(client):
    response = client.get("/mine_block")

    assert response.status_code == 200

    assert response.json['Blockchain']=='New block was mined!'
    assert response.json['current_complexity']==4
    assert response.json['index']==2
    assert isinstance(response.json['nonce'], int)
    assert isinstance(response.json['previous_hash'], str)
    assert len(response.json['previous_hash']) == 64
    assert response.json['previous_hash'][:4]=='0000'
    assert isinstance(response.json['timestamp'], str)
    assert len(response.json['timestamp']) == 26
    assert len(response.json['transactions']) == 1
    assert response.json['transactions'][0]['amount']==1
    assert isinstance(response.json['transactions'][0]['receiver'], str)
    assert len(response.json['transactions'][0]['receiver'])==32
    assert response.json['transactions'][0]['sender']=='BuliCoin network'

# Check that chain with initial block is returned
def test_get_chain(client):
    response = client.get("/get_chain")

    assert response.status_code == 200

    assert response.json['chain'][0]['current_complexity']==4
    assert response.json['chain'][0]['index']==1
    assert response.json['chain'][0]['nonce']==1
    assert response.json['chain'][0]['prev_hash']=='0'
    assert len(response.json['chain'][0]['timestamp']) > 0
    assert len(response.json['chain'][0]['transactions']) == 0
    assert response.json['length'] == 1


# Check validity response on blockchain with only initial block is True
def test_validation(client):

    response = client.get("/validate")

    assert response.status_code == 200
    assert response.json['Chain valid']==True

def test_add_transaction(client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'sender': 'Martin',
        'receiver': 'Sylvie',
        'amount': 1258
    }
    url = '/add_transaction'

    response = client.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 201
    assert response.content_type == mimetype
    assert response.json['message'] == "This transaction will be added to block 2"
