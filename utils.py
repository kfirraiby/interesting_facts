import openai
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta
from googlesearch import search

openai.api_key = " "


# get fact from text
def chatgpt(text, prompt):
    model_engine = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "user",
             "content": f"read the following text '{text}' and give me the 2 most significant facts in this text that "
                        f"relates to {prompt}.print only the relevant facts in a short sentences, if None dont points"
                        f" anything"}
        ])

    message = response.choices[0]['message']
    return "{}: {}".format(message['role'], message['content'])


# choose the best fact
def chatgpt_top_answer(text, prompt):
    model_engine = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "user",
             "content": f"read the following text (python dictionary format)'{text}', where the keys are urls and the "
                        f"values are facts from the url. please  print the fact (value) that is the most informative "
                        f"and relates to {prompt}. please print also the relevant url. print it in the format of "
                        f"'value -> url' meaning only the fact itself and the url, do not add any more text"}
        ])

    message = response.choices[0]['message']
    return "{}: {}".format(message['role'], message['content'])


# get main text from the url
def scrape_url(url):
    text = ''
    # opening the url for reading
    html = requests.get(url).text

    # parsing the html file
    htmlParse = BeautifulSoup(html, 'html.parser')

    # getting all the paragraphs
    for para in htmlParse.find_all("p"):
        text += para.get_text()

    return text


# prompt based query
def google_query(query):
    urls_list = []
    last_month = datetime.now() - relativedelta(years=1)
    date = format(last_month, '%B %Y')
    query += ' ' + f'after:{date} '
    for url in search(query, tld="co.in", num=1, stop=2, pause=2):
        urls_list.append(url)

    return query, urls_list



