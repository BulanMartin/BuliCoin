from blockchain import Blockchain
import datetime
from urllib.parse import urlparse
from collections import OrderedDict
import hashlib
import json

class BuliCoin(Blockchain):

    def __init__(self):
        # Add transactions to the block structure and let parent class create the first block
        # using overridden method create_block()

        self.transactions = []
        super().__init__()
        
        self.nodes = set()

    def create_block(self, nonce, prev_hash):
        # Create new block and append it to the blockchain
        # Override parent method (transactions added)

        block = OrderedDict({
                 'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'prev_hash': prev_hash,
                 'current_complexity': self.leading_zeros,
                 'transactions': self.transactions
                })

        self.transactions = []
        
        self.chain.append(block)
        return block

    def hash(self, prev_block, nonce):
        # Get SHA256 hash of previous block and nonce number

        # Each key:value pair must be handeled separately so as the key order is preserved (order of
        # elements is not preserved by JSON format)

        transactions_string = ''
        for transaction in prev_block['transactions']:
            transactions_string += str(transaction['sender'])
            transactions_string += str(transaction['receiver'])
            transactions_string += str(transaction['amount'])

        return hashlib.sha256(json.dumps(
            str(prev_block['index']) + 
            str(prev_block['timestamp']) + 
            str(prev_block['nonce']) + 
            str(prev_block['prev_hash']) + 
            str(prev_block['current_complexity']) + 
            transactions_string +
            str(nonce), sort_keys=True).encode()).hexdigest()

    def add_transaction(self, sender, receiver, amount):
        # Append new transaction to the transactions parameter,
        # which will be added to the next block

        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

        previous_block = self.get_prev_block()
        return previous_block['index'] + 1

    def add_node(self, address):
        # Add new node in the network (combination of IP and port)

        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
