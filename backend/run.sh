#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run the command
python manage.py "$@"
