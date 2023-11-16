from instagrapi import Client
from instagrapi.types import Usertag
import time

# Replace 'your_username' and 'your_password' with your Instagram credentials
username = 'omarelsherif0102'
password = 'Collegeboard@010'

# Create an instance of the Client
client = Client()
client.login(username, password)

username_list = ["yousefawadalla94"]
users_id_list = []
thread_id_list = []

for user in username_list:
    user_id = client.user_id_from_username(user)
    users_id_list.append(user_id)


# Get the media
media_pk = client.media_pk_from_url(url="https://www.instagram.com/p/CQ9z0wYnLpC/")
media_caption = client.media_info(media_pk).dict()['caption_text']
print(media_caption)


# # Upload the photo
# media = client.photo_upload(
#     path="linkedin community post.jpeg",
#     caption="Join GeeksHub",
#     usertags=[Usertag(user=user, x=0.5, y=0.5)]
# )