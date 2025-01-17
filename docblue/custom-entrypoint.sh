#!/bin/bash

# Python packages are installed under virtual environment. Activate venv first to see them while bash
# Python project must be executed with venv activated manually in bash

echo "custom-entrypoint.sh: Started"
set -e # Exit on errors. Easier for debuting

# Remove the existing virtual environment if it exists
if [ -d "/home/bor/docblue/myenv" ]; then
  echo "custom-entrypoint.sh: Removing existing virtual environment..."
  rm -rf /home/bor/docblue/myenv
fi

# Create the virtual environment if it doesn't exist
if [ ! -d "/home/bor/docblue/myenv" ]; then
  echo "custom-entrypoint.sh: Creating virtual environment..."
  if python3 -m venv /home/bor/docblue/myenv; then
    echo "custom-entrypoint.sh: Virtual environment created!"
  else
    echo "custom-entrypoint.sh: Failed to create virtual environment!" >&2
    exit 1
  fi
else
  echo "custom-entrypoint.sh: Virtual environment already exists."
fi

# Activate the virtual environment
# do i need to activate if it's being activated in .bashrc?
#if [ -f "/home/bor/docblue/myenv/bin/activate" ]; then
#  echo "custom-entrypoint.sh: Activating virtual environment..."
#  source /home/bor/docblue/myenv/bin/activate
#else
#  echo "custom-entrypoint.sh: Activation script not found!" >&2
#  exit 1
#fi

# Install python tools
echo "custom-entrypoint.sh: Installing python tools..."
#pip install --force-reinstall pip textual textual-dev Flask
pip install pip textual textual-dev

# Modify .bashrc to automatically activate the virtual environment on every bash session
echo "source /home/bor/docblue/myenv/bin/activate" >> /root/.bashrc

# Keep the container running
tail -f /dev/null
