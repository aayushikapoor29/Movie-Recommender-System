#!/bin/bash

# Update package lists and install dependencies
echo "Updating package lists..."
sudo apt-get update

# Install Python and pip if not already installed
echo "Installing Python and pip..."
sudo apt-get install -y python3 python3-pip

# Install necessary Python packages
echo "Installing required Python packages..."
pip3 install -r requirements.txt

# Notify user of completion
echo "Setup complete. You can now run your Streamlit app."
