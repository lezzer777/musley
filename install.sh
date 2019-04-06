#!/bin/bash
printf "This script will install dependencies for Musley\nWait a few seconds untill the scripts ends.\n---\n"

echo "Installing termcolor - a python libary for text coloring."
sudo pip install termcolor >/dev/null
echo "Success. You can run python musley.py now."
