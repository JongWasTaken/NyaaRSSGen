#!/bin/sh

echo "Updating..."
git fetch --all
git reset --hard origin/master

echo "Launching..."
python ./mkRSS.py
