Node of Quantum Safe Coin (QSC)

    Host a node of QSC and mine the coins with CPUs.

OS: Ubuntu


Installation:

    Requirements: Docker

    Steps:

        1) download the repository.

        2) cd QSC-Node

        3) obtain your wallet address (to see the following section) and revise the script in "./QSC-Node/start.sh". It looks like:
        
            "python3 src/qsc/main.py --debug --network-type mainnet --mining_intensity 0.9 --miningAddress q000a00283951e3dc80bfad24da5b6615bea8662d72a3d4f5657e2ad6805b7c0d8b5ff12aa3ae5f"
            
            You need to replace "q000a00283951e3dc80bfad24da5b6615bea8662d72a3d4f5657e2ad6805b7c0d8b5ff12aa3ae5f" with your address;

            You can turn off "--debug"; 
            
            You can adjust mining inensity based on your CPU computation power and desired energy comsuption.
        
        4) sudo bash build_docker.sh

        5)  (a) sudo bash start_docker.sh 

            (b) python3 src/qsc/main.py --network-type mainnet --mining_intensity 0.9 --miningAddress your_QSC_wallet_address 
            
            (c) alternatively if you want the Docker container to run in the detached mode, see the script "start_docker_b.sh"



How to get your QSC wallet address for mining?

    1) download the QSC PyWallet from: https://github.com/qsc-fdn/QSC-PyWallet.git

    2) install it.

    3) run it to pop up the GUI -> wizard -> create wallet -> mark down your hexseed and your wallet address.


About QSC:

   To see the QSC white paper: 
   
   https://github.com/qsc-fdn/White-Paper


Support: 

    qsc.fdn@gmail.com