from dotenv import dotenv_values
import streamlit, sqlite3
import google.generativeai as gemini

# load environment file
config = dotenv_values('.env')

# get google gemini api key
uri = config['GOOGLE_API_KEY']

# configure generative ai key
gemini.configure(api_key=uri)


# loads gemini model, sends prompt to model and provide sql query as response
def get_llm_response(user_input, llm_prompt):
    model = gemini.GenerativeModel('gemini-pro')
    llm_response = model.generate_content([llm_prompt[0], user_input])
    return llm_response.text


# retrieve query from db
def get_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()
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


# create streamlit app
streamlit.set_page_config(page_title="Text Generation", page_icon=":")
streamlit.header("Gemini App to retrieve SQL data from prompts")
question = streamlit.text_input('Enter your question: ', key='input')
submit = streamlit.button('submit')

if submit:
    gemini_response = get_llm_response(question, prompt)
    sql_response = get_sql_query(gemini_response, 'student.db')
    streamlit.subheader('The response is: ')
    for row in sql_response:
        print(row)
        streamlit.header(row)
