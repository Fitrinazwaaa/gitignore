import requests
from pprint import pprint

r = requests.get("https://jsonplaceholder.typicode.com/posts")
data = r.json()
pprint(data)

post = {
    'body': "Leoren ipsum",
    'title':"Title",
    'userId': 5,
}

req = requests.post("https://jsomplaceholder.typicode.com/posts", json=post)
print(req.json())

update_post = post
update_post['id'] = 5

req = requests.put(
    'https://jsonplaceholder.typicode.com/posts/5', json=update_post)
print(req.json())

"""
Client -> API -> Backend(Server)

web Method:

Get -> Ambil Data
Post -> Buat Data di Server
Patch/Put -> Update data di server
Delete -> Hapus data di server
"""