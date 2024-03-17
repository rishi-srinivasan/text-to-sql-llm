# LLM Application that returns SQL queries from text

Python 3.11 based LLM app that creates a SQL lite database, stores records into it.

Uses Google Gemini API to retrieve data from the database using english prompts from the user.

Frontend is built on streamlit.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.
Run the setup file [setup.sh]() to create .env file, install requirements and create the readme file.

```bash
sh setup.sh
```

## Environmental Variables

Below environment variables need to be saved in a .env file
```
GOOGLE_API_KEY="your key here"
```

## Deploy

```python
python3 sqlLite.py
streamlit gemini.py
```