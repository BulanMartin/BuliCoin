from flaskr.blockchain import Blockchain
from collections import OrderedDict
import datetime
import json

# Check Blockchain() class init function
def test_init():
    test_chain = Blockchain()

    assert isinstance(test_chain.chain[0], OrderedDict)

    assert test_chain.chain[0]['current_complexity'] == 4
    assert test_chain.chain[0]['nonce'] == 1
    assert test_chain.chain[0]['index'] == 1
    assert isinstance(test_chain.chain[0]['timestamp'], str)
    assert len(test_chain.chain[0]['timestamp']) == 26
    assert len(test_chain.chain) == 1
    assert test_chain.leading_zeros == 4

# Check that previous block is returned
def test_get_prev_block():
    test_chain = Blockchain()

    prev_block = test_chain.get_prev_block()

    assert isinstance(prev_block, OrderedDict)

    assert prev_block['current_complexity'] == 4
    assert prev_block['nonce'] == 1
    assert prev_block['index'] == 1
    assert isinstance(prev_block['timestamp'], str)
    assert len(prev_block['timestamp']) == 26

# Test block mining functionality
def test_mine_block():
    test_chain = Blockchain()

    prev_block = test_chain.get_prev_block()
    nonce = test_chain.proof_of_work(prev_block)
    prev_hash = test_chain.hash(prev_block, nonce)
    block = test_chain.create_block(nonce, prev_hash)

    assert block['index']== 2
    assert isinstance(block['timestamp'], str)
    assert len(block['timestamp']) == 26
    assert block['current_complexity'] == 4