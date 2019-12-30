import requests
from bs4 import BeautifulSoup as Bs

URL = 'https://54-215-139-63-social.vulnerablesites.net/InstaFriends/users/profile/1'
COOKIE = 'lQbvyUT5pWLoMf03DRE57tnOx3xetg943e5+vf4UAOtBu8bQ'


def is_sessison_valid():
    cookie = {'instafriends_session_id': COOKIE}
    page = requests.get(URL, cookies=cookie)
    soup = Bs(page.text, 'html.parser')
    print(soup.prettify())



is_sessison_valid()
