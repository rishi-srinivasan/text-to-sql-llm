#! /bin/bash

touch .env && touch README.md && touch requirements.txt && touch .gitignore

echo "python-dotenv\streamlit\ngoogle-generativeai\nsqlite3" > requirements.txt

echo ".env\n.idea\nvenv/" > .gitignore

pip install -r requirements.txt

pip freeze > requirements.txt

pip install --upgrade pip