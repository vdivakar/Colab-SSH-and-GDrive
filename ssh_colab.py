
###################################################################
# Install all the preferred environment utilities and dependencies
# For GPU: Runtime -> Change runtime type -> Select GPU
###################################################################

apt-get install vim
apt-get install tree
git clone https://github.com/chentinghao/download_google_drive.git


nvidia-smi

################################################################
# Important step if you want to save your progress.
# cd to the project directory inside your gdrive and work there
# cd /content/gdrive/My Drive/'
################################################################

from google.colab import drive
drive.mount('/content/gdrive/')

################################################################
# Download ngrok and run
# Required: ngrok token & public key of your local machine
################################################################

wget https://gist.githubusercontent.com/archie9211/ae3c8411da88ae8b2a05b0ee1a4fd412/raw/ee1a6e78fc498ad6d4830cd2eb6033839235ea8a/colab-ssh-jupyter.sh
bash colab-ssh-jupyter.sh
