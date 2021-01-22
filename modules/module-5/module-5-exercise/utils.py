import requests
from bs4 import BeautifulSoup
import re


def get_transcript():

    url = "https://trumpwhitehouse.archives.gov/briefings-statements/remarks-president-trump-state-union-address-3/"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'lxml')
    transcript_html = soup.find("div", class_="page-content__content editor")

    transcript_text = transcript_html.getText()

    transcript_text = re.sub(r'\(.*\)', '', transcript_text)

    transcript_text = re.sub(r'AUDIENCE:.*\n', '', transcript_text) # Removes audience comments

    transcript_text = re.sub(r'\s+', ' ', transcript_text) # Removes extra whitespace

    transcript_text = transcript_text.replace('THE PRESIDENT:', '') # Removes THE PRESIDENT speaker ID

    return transcript_text