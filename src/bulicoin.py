from blockchain import Blockchain
import datetime
from urllib.parse import urlparse

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

        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'prev_hash': prev_hash,
                 'current_complexity': self.leading_zeros,
                 'transactions': self.transactions
                }

        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        # Append new transaction to the transactions parameter,
        # which will be added to the next block

        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

    def add_node(self, address):
        # Add new node in the network (combination of IP and port)

        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

coin = BuliCoin()
print(str(coin.chain))