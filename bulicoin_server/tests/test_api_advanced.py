import json

# Check api functions combined with mining
def test_mining(client):
    response = client.get("/get_chain")

    assert response.status_code == 200
    assert response.json['length'] == 1

    client.get("/mine_block")
    client.get("/mine_block")

    # check that chain length is 3
    response = client.get("/get_chain")
    assert response.json['length'] == 3

    response = client.get("/validate")

    assert response.status_code == 200
    assert response.json['Chain valid']==True

    # increase complexity to 5 leading zeros
    client.get("/complexity/5")

    # add 2 transactions
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

    data2 = {
        'sender': 'John',
        'receiver': 'Emma',
        'amount': 52
    }

    response = client.post(url, data=json.dumps(data2), headers=headers)

    # mine next block
    client.get("/mine_block")

    # check that new block[3] has increased complexity and 2 new transactions
    response = client.get("/complexity/")

    assert response.status_code == 200
    assert response.json['Current number of leading zeros ']==5

    response = client.get("/get_chain")

    assert isinstance(response.json['chain'][3]['prev_hash'], str)
    assert len(response.json['chain'][3]['prev_hash']) == 64
    assert response.json['chain'][3]['prev_hash'][:5]=='00000'

    assert response.json['chain'][3]['transactions'][0]['sender']=='Martin'
    assert response.json['chain'][3]['transactions'][0]['receiver']=='Sylvie'
    assert response.json['chain'][3]['transactions'][0]['amount']==1258

    assert response.json['chain'][3]['transactions'][1]['sender']=='John'
    assert response.json['chain'][3]['transactions'][1]['receiver']=='Emma'
    assert response.json['chain'][3]['transactions'][1]['amount']==52

    assert response.json['chain'][3]['transactions'][2]['sender']=='BuliCoin network'

    response = client.get("/validate")
    assert response.json['Chain valid']==True

    # decrease complexity to 2 leading zeros
    client.get("/complexity/2")

    client.get("/mine_block")

    data3 = {
        'sender': 'Nick',
        'receiver': 'Bruce',
        'amount': 99
    }
    client.post(url, data=json.dumps(data3), headers=headers)
    client.get("/mine_block")

    # validate new blocks with decreased complexity
    response = client.get("/get_chain")
    assert response.json['length'] == 6

    assert response.json['chain'][5]['transactions'][0]['sender']=='Nick'
    assert response.json['chain'][5]['transactions'][0]['receiver']=='Bruce'
    assert response.json['chain'][5]['transactions'][0]['amount']==99

    response = client.get("/validate")
    assert response.json['Chain valid']==True

    # increase complexity back to 4 leading zeros
    client.get("/complexity/4")

    data4 = {
        'sender': 'Jan',
        'receiver': 'Mark',
        'amount': 1000
    }
    client.post(url, data=json.dumps(data4), headers=headers)

    client.get("/mine_block")

    # validate new block with original complexity
    response = client.get("/get_chain")
    assert response.json['length'] == 7

    assert response.json['chain'][6]['transactions'][0]['sender']=='Jan'
    assert response.json['chain'][6]['transactions'][0]['receiver']=='Mark'
    assert response.json['chain'][6]['transactions'][0]['amount']==1000

    response = client.get("/validate")
    assert response.json['Chain valid']==True