#!/bin/sh

echo "Updating..."
git pull

echo "Launching..."
python ./mkRSS.py
