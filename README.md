# blkchn-buildingblocks
a testnet blockchain using Puppeth, Geth, &amp; the Clique Proof of Authority algorithm

---
## Setup
links:
- Download & install the MyCrypto Desktop App for your OS at https://download.mycrypto.com/
- Download the most recent **GETH & TOOLS** for your OS and version (32 or 64 bit )at https://geth.ethereum.org/downloads/
    - extract the contents to a location easy to reach and rename the folder blockchain-tools or something similar
---
## Code Guide for blockchain setup
1. Block Genesis (press enter after completing each step)
    - `./puppeth` 
        - network name: thecoin
        - configure new genesis from scratch: option 2;1
        - choose consensus algorithm: clique- PoA
        - paste wallet addresses to be prefunded without the first 0x 
        - choose **NO** for prefund with 1 wei
        - Chain ID:777 & password: passthecoin
        - Blocktime: 10 seconds
        - when genesis is completed, `manage existing genesis` and then `export genesis configurations`

2. Create Accounts/Nodes
    - `./geth --datadir node1 account new` 
    - `./geth --datadir node2 account new `
    - "use geth to create a data directory for each node's new account information"

3. Initialize & Mine (the two lines of command line code will be run in separate windows; one for node1 & one for node2)
    - Init
        - `./geth --datadir node1 init thecoin.json`
        - `./geth --datadir node2 init thecoin.json`
    - Mine
        - ` ./geth --datadir node1 --mine --miner.threads 1 `
            - **IMMEDIATELY** copy the self-enode from the first node and paste it when mining node2 as below

        - `./geth --datadir node2 --port 30304 --rpc --bootnodes "<enode>" --ipcdisable`
        - make sure where it says port, the number is different from the one from the enode of node1

Congrats! you have started both nodes. Keep them running during the next set of steps.

---
## MyCrypto Setup and Transaction Generation

Network Setup
- In the MyCrypto app, change network to "Add Custom Node" then create the node using information setup from the block genesis. 
![change network](./scshts/2.JPG)


- The network should be set to custom, currency to ETH, and chainID is the same from the genesis. Save & Use when finished.
    - Note the URL is the same as the sample just **http://** instead of https://.
    ![custom node setup](./scshts/1.JPG)

Wallet Setup
- In Create New Wallet, select Generate a Wallet and then choose Mnemonic Phrase on the following screen. Save the phrase.

Accessing the Wallet
- In View & Send, choose PrivateKey and then enter it on the next screen. 

Transaction
- Select Send Ether from the top bar, then input the address to send ETH to and the amount to send. 
- Feel free to mess with the fees, just note that in real transactions paying higher fees will usually equate to a better probability your transaction is verified on the blockchain. Hit send and then confirm on the next popup.
![send transaction](./scshts/7.JPG)

- After successfully sending the transaction, a TX status green box will appear at the bottom with a hash indicating the transaction. 
![send transaction](./scshts/8.JPG)

-This can be seen in terminal window as well
![send transaction](./scshts/9.JPG)

-And finally in the other wallet
![send transaction](./scshts/10.JPG)