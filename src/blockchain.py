import datetime
import hashlib
import json

class Blockchain:

    def __init__(self):

        self.chain = []             # Chain variable
        self.leading_zeros = 4      # Complexity of block mining algorithm (number of leading zeros)
        self.create_block(nonce = 1, prev_hash = '0')   # Create first block of the blockchain (no previous hash, nonce not relevant)
        
    def create_block(self, nonce, prev_hash):
        # Create new block and append it to the blockchain

        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'prev_hash': prev_hash,
                 'current_complexity': self.leading_zeros
                }

        self.chain.append(block)
        return block

    def get_prev_block(self):
        # Returns previous block of the blockchain

        return self.chain[-1]

    def proof_of_work(self, prev_block):
        # Variate nonce and combine it with previous block until the resulting hash has required number of leading zeros

        nonce = 1
        check_nonce = False
        while check_nonce == False:
            hash_operation = hashlib.sha256(json.dumps(str(prev_block) + str(nonce), sort_keys=True).encode()).hexdigest()

            if hash_operation[:self.leading_zeros] == self.leading_zeros*'0':
                check_nonce = True
            else:
                nonce += 1

        return nonce

    def hash(self, prev_block, nonce):
        # Get SHA256 hash of previous block and nonce number

        return hashlib.sha256(json.dumps(str(prev_block) + str(nonce), sort_keys=True).encode()).hexdigest()


    def validate(self, chain):
        # Loop through the blockchain and check its validity

        prev_block = chain[0]
        block_index = 1

        while block_index < len(chain):

            block = chain[block_index]
            if block['prev_hash'] != self.hash(prev_block, block['nonce']):

                # Check that SHA256 hash of nonce of each block combined with previous block matches
                # with 'prev_hash' value of the current block

                return False

            nonce = block['nonce']
            hash_operation = hashlib.sha256(json.dumps(str(prev_block) + str(nonce), sort_keys=True).encode()).hexdigest()

            if hash_operation[:block['current_complexity']] != block['current_complexity']*'0':
                
                # Check that SHA256 hashes of all blocks have required complexity (number of leading zeros)

                return False

            prev_block = block
            block_index += 1

        return True

