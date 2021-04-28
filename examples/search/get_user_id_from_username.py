import os

from instauto.api.client import ApiClient
from instauto.api.actions import search as se

if __name__ == '__main__':
    if os.path.isfile('./.instauto.save'):
        client = ApiClient.initiate_from_file('./.instauto.save')
    else:
        client = ApiClient(username=os.environ.get("INSTAUTO_USER") or "your_username", password=os.environ.get("INSTAUTO_PASS") or "your_password")
        client.log_in()
        client.save_to_disk('./.instauto.save')

    s = se.Username.create("instapowr", 1)
    resp = client.search_username(s).json()
    user_id = resp['users'][0]['pk']
