#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get upgrade
sudo apt-get install nginx
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "38i location \/hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
