from instagrapi import Client
from instagrapi.types import Usertag


username = 'omarelsherif0101'
password = 'Collegeboard@010#instagram'

# Initialize the client
cl = Client()
cl.login(username, password)

# # Get user information
# user = cl.user_info_by_username(username)

# # Upload the photo
# media = cl.photo_upload(
#     path="linkedin community post.jpeg",
#     caption="Join GeeksHub",
#     usertags=[Usertag(user=user, x=0.5, y=0.5)]
# )