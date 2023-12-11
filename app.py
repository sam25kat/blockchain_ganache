from flask import Flask, render_template
from web3 import Web3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_code')
def run_python_code():

    ganache_url = "HTTP://127.0.0.1:7545"

    web3 = Web3(Web3.HTTPProvider(ganache_url))

    account_1 = "0x76eDcfb1Cc0aeAC4814745a6f4B97C0402D68669"  # sender
    account_2 = "0x23290711A1fe35D69c52628511902808F6D3666B"  # receiver
    account_3 = "0x463e20203A1351CB5Acafc2584792D1Dd6401ef2"

    private_key = "0xb07d87c0439629fe1435c8dfb3c4e3b81ea458531d36a7fe90bed997dad6297d"

    nonce = web3.eth.get_transaction_count(account_2)

    tx = {
        'nonce': nonce,
        'to': account_3,
        'value': web3.to_wei(50, 'ether'),  # Corrected here
        'gas': 21000,
        'gasPrice': web3.to_wei('50', 'gwei')
    }

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    #print(web3.toHex(tx_hash))  # Corrected here
    result = web3.to_hex(tx_hash)  
    return result

if __name__ == '__main__':
    app.run(debug=True)