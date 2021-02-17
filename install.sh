#!/bin/bash
echo "installing dependencies"
sudo apt install python3-tk
echo "installing"
mkdir $HOME/.aptgui
echo "copying files"
cp index.py ~/.aptgui
cp aptgui /usr/bin
echo "making executable"
sudo chmod +x /usr/bin/aptgui
echo "installed to /usr/bin/aptgui"

