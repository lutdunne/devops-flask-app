#!/bin/bash

sudo apt update -y && sudo apt upgrade -y

sudo apt install -y nano vim python-is-python3 python3-venv python3-pip

python3 -m venv /home/vagrant/my_venv
source /home/vagrant/my_venv/bin/activate

pip install flask

nohup python /vagrant/hello.py > /home/vagrant/flask.log 2>&1 &
