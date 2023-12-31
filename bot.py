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

def get_direct_messages_from_users(users_id_list):
    messages_list = []
    for user in users_id_list:
        direct_messages = client.direct_thread_by_participants(user_ids=[user]) 
        
        thread_id = direct_messages['thread']['thread_id']
        thread_id_list.append(thread_id)
        print(f"Thread ID List: {thread_id_list}")

        message = direct_messages['thread']['items'][0].dict()
        messages_list.append(message)
        print(f"messages Received: {messages_list}")
    return messages_list

def share_message_as_story(): #message_id
    # Retrieve the media (photo or video) from the direct message
    # message = client.direct_v2_item(message_id)
    message = get_direct_messages_from_users(users_id_list)[0]

    media = message.get('media', [])

    # Check if the message has media
    if media:
        # Upload the same media to your story
        for item in media:
            media_type = item.get('media_type')
            media_url = item.get('image_versions2', {}).get('candidates', [])[0].get('url') if media_type == 1 else item.get('video_versions', [])[0].get('url') if media_type == 2 else None

            if media_url:
                if media_type == 1:  # Photo
                    client.photo_upload(media_url, caption="Shared from direct message")
                elif media_type == 2:  # Video
                    # You can use client.video_upload() for videos (requires additional parameters)
                    pass

# Example usage
# Replace 'your_message_id' with the actual ID of the direct message you want to share
# message_id = 'your_message_id'
share_message_as_story()

# username_list = ["asmaa_elsherif_010", "s_a_i_d___mp"]
# users_id_list = []
# thread_id_list = []

# for item in username_list:
#     user_id = client.user_id_from_username(item)
#     users_id_list.append(user_id)

# function to get direct messages from list of users
# def get_direct_messages_from_users(users_id_list):
#     messages_list = []
#     for user in users_id_list:
#         direct_messages = client.direct_thread_by_participants(user_ids=[user]) 
        
#         thread_id = direct_messages['thread']['thread_id']
#         thread_id_list.append(thread_id)

#         message = direct_messages['thread']['items'][0]['text']
#         messages_list.append(message)
#         # print(f"messages Received: {messages_list}")
#     return messages_list

# print(get_direct_messages_from_users(users_id_list), thread_id_list)

# Collect thread ids of direct messages
# for user in users_id_list:
#         direct_messages = client.direct_thread_by_participants(user_ids=[user]) 
        
#         thread_id = direct_messages['thread']['thread_id']
#         thread_id_list.append(thread_id)
# thread_details = client.direct_thread(thread_id=thread_id_list[0])
# link_to_post = thread_details['messages']
# print(f"Thread Details: {link_to_post}")

# Get user information
user = client.user_info_by_username(username)

# Upload the photo
media = client.photo_upload(
    path="linkedin community post.jpeg",
    caption="Join GeeksHub",
    usertags=[Usertag(user=user, x=0.5, y=0.5)]
)

# # Function to handle reposting from personal messages
# def repost_from_messages():
#     # Get direct messages
#     direct_messages = client.direct_v2_inbox()
#     print(f"Direct Messages Received: {direct_messages}")

#     # Loop through messages
#     for message in direct_messages['inbox']['threads']:
#         # Check if the message is from an allowed user
#         if message['users'][0]['username'] in allowed_users:
#             # Extract post information (adjust this based on the actual structure of the message)
#             post_info = extract_post_info(message)

#             # Repost the post to the connected account's feed
#             repost_to_feed(post_info)

#             # Create a story with the reposted post
#             create_story(post_info)

#             # Remove the processed message from the inbox
#             client.direct_v2_thread_hide(message['thread_id'])

# # Function to handle reposting at a specified interval
# def repost_at_interval():
#     while True:
#         # Call the function to repost from messages
#         repost_from_messages()

#         # Wait for the specified interval (e.g., 1 hour)
#         time.sleep(3600)

# # Function to handle reposting from shared accounts
# def repost_from_shared_account(shared_account_username):
#     # Get posts from the shared account
#     shared_account_posts = get_posts_from_account(shared_account_username)

#     # Loop through posts and add to the repost list based on specified parameters
#     for post in shared_account_posts:
#         if meets_repost_criteria(post):
#             add_to_repost_list(post)

# # Example usage
# allowed_users = ['user1', 'user2']  # List of allowed users
# repost_at_interval()  # Start reposting at the specified interval
