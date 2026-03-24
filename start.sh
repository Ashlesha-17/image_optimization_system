#!/bin/bash

# Upgrade pip, setuptools, wheel
pip install --upgrade pip setuptools wheel

# Install all dependencies
pip install -r requirements.txt

# Start Flask app with Gunicorn
gunicorn app:app