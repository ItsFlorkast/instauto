from instauto.api.client import ApiClient
import instauto.api.actions.friendships as fs

client = ApiClient.initiate_from_file('.instauto.save')

user_id = "12345678"
obj = fs.Remove(user_id)
client.follower_remove(obj)

