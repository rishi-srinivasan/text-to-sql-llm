from dotenv import dotenv_values
import os, streamlit, sqlite3
import google.generativeai as gemini

# load environment file
config = dotenv_values('.env')

# get google gemini api key
uri = config['GOOGLE_API_KEY']

# configure generative ai key
gemini.configure(api_key=uri)


# loads gemini model, sends prompt to model and provide sql query as response
def get_response(question, prompt):
    model = gemini.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text


# retrieve query from db
def read_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows


# define the prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!\n
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION\n\n
    For example, Example 1 - How many entries of records are present?, 
    the SQL command will be like this: SELECT COUNT(*) FROM STUDENT;\n
    Example 2 - Show me all the students studying cloud computing class, the SQL command will be like this:
    SELECT * FROM STUDENT where CLASS="Cloud Computing";\n Also the SQL code should not have ``` in the beginning or
    end. The SQL code should not have the word SQL in the output
    """
]