import os

from instauto import ApiClient
from instauto import structs as st
from instauto import post as ps

if __name__ == '__main__':
    if os.path.isfile('./.instauto.save'):
        client = ApiClient.initiate_from_file('./.instauto.save')
    else:
        client = ApiClient(user_name="your_username", password="your_password")
        client.login()
        client.save_to_disk('./.instauto.save')

    post = ps.PostPost.create(
        path='./black_square.jpg',
        source_type=st.WhereToPost.Feed,
        caption='This is an example. Follow me!'
    )

    resp = client.post_post(post, 80)
    print("Success: ", resp.ok)
