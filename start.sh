#!/bin/bash

# Upgrade pip, setuptools, and wheel to make sure pkg_resources is available
pip install --upgrade pip setuptools wheel

# Install all packages from requirements.txt
pip install -r requirements.txt

# Start your Flask app using Gunicorn
gunicorn app:app