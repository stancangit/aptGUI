#!/bin/bash
echo "removing dependencies"
sudo apt remove python3-tk
echo "uninstalling"
sudo rm -d ~/.aptgui
echo "removing copied files"
sudo rm ~/.aptgui/index.py
sudo rm /usr/bin/aptgui
echo "Removed, sad to see you go"
