from instagrapi import Client
import time

# Replace 'your_username' and 'your_password' with your Instagram credentials
username = 'omarelsherif0101'
password = 'Collegeboard@010#instagram'

# Create an instance of the Client
client = Client()
client.login(username, password)

# try: direct_v2_inbox()
direct_messages = client.direct_pending_inbox()
print(f"Direct Messages Received: {direct_messages}")
# for message in direct_messages:
#     print(f"Message: {message.text}")
#     print(f"Sender ID: {message.sender_id}")
#     print(f"Timestamp: {message.timestamp}")
#     print("----------------------------------")
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
