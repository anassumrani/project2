#!/bin/bash     
sudo apt update
sudo apt install python3 python3-pip python3-venv chromium-browser wget unzip-y
sudo apt install -y chromium-browser
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip


python3 -m venv venv 
source venv/bin/activate 
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov.report=html

#initial admin password: 7c2e4bf9d47c4e9d868754c1c9de9b74