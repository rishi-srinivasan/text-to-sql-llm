#! /bin/bash

touch .env && touch README.md && touch requirements.txt && touch .gitignore

echo "python-dotenv\nopenai\nllama-index\npypdf" > requirements.txt

echo ".env\n.idea\nvenv/" > .gitignore

pip freeze > requirements.txt

pip install --upgrade pip

pip install -r requirements.txt