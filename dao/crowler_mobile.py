import re
import requests
from bs4 import BeautifulSoup
from abc import abstractmethod, ABCMeta
# from fake_useragent import UserAgent

USER_AGENT = "Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5S) Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"

def get_soup(link, target_str):
    # headers를 랜덤으로? 아니면 고정으로? 접속량이 많지 않아 고정으로도 괜찮을까?
    html_text = requests.get(link, headers = {'User-Agent' : USER_AGENT}).text
    return BeautifulSoup(html_text, features='html.parser')

def get_board(site, link):
    pass

def get_post(link):
    pass