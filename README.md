# LLM Application that returns SQL data from english prompts

Python 3.11 based LLM app that creates a SQL lite database, stores records into it.

Uses Google Gemini API to retrieve data from the database using english prompts from the user.

The app displays the sql data to users on a streamlit UI.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.
Run the setup file [setup.sh](https://github.com/rishi-srinivasan/text-to-sql-llm/blob/main/setup.sh) to create .env file, readme file, .gitignore.

The setup file also populates .gitignore file, requirements file along with installing requirements.

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