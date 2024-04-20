#!/bin/bash

# Define the virtual environment directory name
VENV_DIR="venv"

# Check if the virtual environment directory exists
if [ -d "$VENV_DIR" ]; then
    echo "Existing virtual environment found. Deleting..."
    # Remove the existing virtual environment directory
    rm -rf $VENV_DIR
    echo "Existing virtual environment deleted."
fi

echo "Creating a new virtual environment..."
# Create the virtual environment
python3 -m venv $VENV_DIR
echo "Virtual environment created."

# Activate the virtual environment
echo "Activating the virtual environment..."
source $VENV_DIR/bin/activate

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    # Install dependencies
    pip install -r requirements.txt
    echo "Dependencies installed."
else
    echo "No requirements.txt found. Skipping installation of dependencies."
fi

# Function to check if the script was called with an argument to keep the venv activated
function check_activation_flag {
    echo "Checking flags: $@"
    local found_active_flag=false
    for arg in "$@"
    do
        if [[ "$arg" == "-a" || "$arg" == "--activate" ]]; then
            found_active_flag=true
            break
        fi
    done
    
    if [ "$found_active_flag" = true ]; then
        echo "The virtual environment will remain active. To deactivate, use the 'deactivate' command."
        return
    else
        deactivate
        echo "Virtual environment deactivated."
    fi
}

# Check activation flag
check_activation_flag "$@"

echo "Setup complete."
