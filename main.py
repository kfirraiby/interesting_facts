from utils import *
from collections import defaultdict


def run():
    answers = defaultdict(dict)
    prompt = input("Type a query: ")
    query, urls_list = google_query(prompt)
    for u in urls_list:
        text = scrape_url(u)
        max_input_tokens_text = ' '.join(text.split(' ')[:3000])
        answers[u] = chatgpt(max_input_tokens_text, prompt)
    print(chatgpt_top_answer(str(answers), prompt))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

