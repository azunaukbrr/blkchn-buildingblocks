import os
from web3 import Web3
from dotenv import load_dotenv
import os
from eth_account import Account
from pathlib import Path
from getpass import getpass

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
pkey = os.getenv("PK")
w3.eth.getBalance("0xd5eaF158037CC0892FC0D23C8D6473f23Ce5C8EF")

account_one = Account.from_key(pkey)

with open(Path("/f/adocs/fintech/blkchnpy")) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(
        encrypted_key, getpass("enter store password")
    )

print(account_one.address)



def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address,
        "to": recipient,
        "value":amount
        }
    )
    return {
        "chainID":333,
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount
        (account.address),
    }


def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    print(result.hex())
    return result.hex()

# send_tx(account_one)

# print(w3.eth.getBalance(account_two.address))