#!/bin/bash

# Node Setup Script
# © 2026 Ervin Remus Radosavlevici

# Install Node.js and npm
echo "Installing Node.js..."
apt-get install -y nodejs npm

# Install project dependencies
echo "Installing project dependencies..."
npm install

# Set up environment
echo "Environment ready."

# Verify
echo "Verification:"
node -v
npm -v

echo "Node setup complete."