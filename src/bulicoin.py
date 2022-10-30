from blockchain import Blockchain
import datetime

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

coin = BuliCoin()
print(str(coin.chain))