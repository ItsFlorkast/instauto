import os

from instauto.api.client import ApiClient
from instauto.api.actions import post as ps

if __name__ == '__main__':
    if os.path.isfile('./.instauto.save'):
        client = ApiClient.initiate_from_file('./.instauto.save')
    else:
        client = ApiClient(username=os.environ.get("INSTAUTO_USER") or "your_username", password=os.environ.get("INSTAUTO_PASS") or "your_password")
        client.log_in()
        client.save_to_disk('./.instauto.save')

    like = ps.Unlike.create(
        media_id="1734612737423614055_6400760974"
    )
    client.post_unlike(like)
