#!/bin/bash

sudo apt update -y && sudo apt upgrade -y

sudo apt install -y nano vim python-is-python3 python3-venv python3-pip

python -m venv ~/my_venv
source ~/my_venv/bin/activate

pip install flask
