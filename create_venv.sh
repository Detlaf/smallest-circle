#!/bin/bash

echo "Setting up virtual environment"
pip install virtualenv
virtualenv venv
source ./venv/bin/activate
echo "Installing all the necessary packages"
pip install -r requirements.txt

# Uncomment below lines if start.py doesn't display any graphics
#sudo apt-get install tcl-dev tk-dev python-tk python3-tk
#pip uninstall matplotlib
#git clone https://github.com/matplotlib/matplotlib.git
#cd matplotlib
#python setup.py install
