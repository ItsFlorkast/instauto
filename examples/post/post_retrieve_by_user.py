from instauto.api.client import ApiClient
from instauto.api.actions.structs.post import PostRetrieveByUser
from instauto.api.actions.structs.search import SearchUsername
import os


if __name__ == '__main__':
    if os.path.isfile('./.instauto.save'):
        client = ApiClient.initiate_from_file('./.instauto.save')
    else:
        client = ApiClient(user_name="your_username", password="your_password")
        client.login()
        client.save_to_disk('./.instauto.save')

    s = SearchUsername.create('instagram', 1)
    resp = client.search_username(s).json()
    user = resp['users'][0]
    user_id = user['pk']

    r = PostRetrieveByUser.create(user_id)

    obj, result = client.post_retrieve_by_user(r)
    retrieved_items = []

    # retrieve the first 20 posts
    while result and len(retrieved_items) < 20:
        retrieved_items.extend(result)
        obj, result = client.post_retrieve_by_user(obj)
        print(f"Retrieved {len(result)} new posts!")
    print(f"Retrieved a total of {len(retrieved_items)} posts!")