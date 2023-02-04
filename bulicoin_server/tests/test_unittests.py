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

