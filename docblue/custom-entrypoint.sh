#!/bin/bash

set -e # Exit on errors. Easier for debuting

# Modify .bashrc to automatically activate the virtual environment on every bash session
# Pass path to venv
echo "source /venv/bin/activate" >> /root/.bashrc

# Keep the container running
tail -f /dev/null
