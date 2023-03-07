from dotenv import load_dotenv
import os
from web3 import Web3


load_dotenv()

api_key = os.getenv('API_KEY')

# Connect to the Ethereum network
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/{}'.format(api_key)))

# Get the latest block number
latest_block = w3.eth.block_number

# Get the latest block
latest_block_obj = w3.eth.get_block(latest_block)

# Find the transaction with the highest value in the latest block
max_value_tx = None
max_value = 0
for tx_hash in latest_block_obj.transactions:
    tx = w3.eth.get_transaction(tx_hash)
    if tx.value > max_value:
        max_value = tx.value
        max_value_tx = tx
print("block: {}, value: {} eth, tx_id: {}".format(latest_block, max_value//1e18, max_value_tx.hash.hex()))

