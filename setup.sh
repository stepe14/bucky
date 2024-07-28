#!/bin/bash

# Define project directories
PROJECT_ROOT=$(pwd)
VENV_DIR="$PROJECT_ROOT/venv"

echo "Setting up BUCKY_V1 project..."

# Step 1: Create a virtual environment
if [ -d "$VENV_DIR" ]; then
  echo "Virtual environment already exists."
else
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 3: Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Step 4: Install system dependencies using Chocolatey
if [[ "$OSTYPE" == "msys" ]]; then
  echo "Installing system dependencies using Chocolatey..."
  choco install flac -y
else
  echo "System dependencies installation skipped (not Windows)"
fi

echo "Setup complete. You can now run your Flask application using 'python src/app.py'."


