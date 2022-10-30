from flask import Flask, jsonify, request
from bulicoin import BuliCoin
from uuid import uuid4

# Initiate Flask server

app = Flask(__name__)

node_address = str(uuid4()).replace('-', '')
# Create blockchain
blockchain = BuliCoin()

# Mine a new block and add it to the end of the blockchain
@app.route('/mine_block', methods=['GET'])
def mine_block():

    # Get previous block
    prev_block = blockchain.get_prev_block()

    # Calculate nonce so as to get hash with required number of leading zeros
    nonce = blockchain.proof_of_work(prev_block)

    # Get has of the previous block and current nonce
    prev_hash = blockchain.hash(prev_block, nonce)

    # Give miner 1 BuliCoin
    blockchain.add_transaction(sender = "BuliCoin network", receiver = node_address, amount = 1)

    # Create new block
    block = blockchain.create_block(nonce, prev_hash)

    # Prepare dictionary for the HTTP response
    response = {'Blockchain': 'New block was mined!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'nonce': block['nonce'],
                'previous_hash': block['prev_hash'],
                'current_complexity': block['current_complexity'],
                'transactions': block['transactions']}

    # Return response as JSON file
    return jsonify(response), 200


# Return current blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}

    return jsonify(response), 200

# Set complexity (number of leading zeros), get current complexity if no number is provided
@app.route('/complexity/', methods=['GET'])
@app.route('/complexity/<int:leading_zeros>', methods=['GET'])
def set_complexity(leading_zeros = None):

    # Set leading zeros parameter of the blockchain
    if leading_zeros:
        blockchain.leading_zeros=leading_zeros

        response = {'Leading zeros set to ': blockchain.leading_zeros}
        return jsonify(response), 200

    else:

        # If no new  complexity value is provided, return current complexity
        response = {'Current number of leading zeros ': blockchain.leading_zeros}
        return jsonify(response), 200

# Validate blockchain and return true if the chain is valid
@app.route('/validate', methods=['GET'])
def validate():

    response = {'Chain valid': blockchain.validate(blockchain.chain)}

    return jsonify(response), 200

# Add new transaction
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']

    if not all (key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing', 400

    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message': f'This transaction will be added to block {index}'}
    return jsonify(response), 201

# Run server
app.run(host = '0.0.0.0', port = 5000)