#!/bin/bash

echo "🚀 SETUP TFT BOT..."

# tạo venv
python3 -m venv venv
source venv/bin/activate

# cài lib
pip install -r requirements.txt

# load env
export $(grep -v '^#' .env | xargs)

# run bot
echo "🔥 BOT STARTING..."
python bot/main.py