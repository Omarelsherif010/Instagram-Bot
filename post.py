from instagrapi import Client
from instagrapi.types import Usertag
import time

# Replace 'your_username' and 'your_password' with your Instagram credentials
username = 'omarelsherif0102'
password = 'Collegeboard@010'

# Create an instance of the Client
client = Client()
client.login(username, password)

username_list = ["danilgreen"]
users_id_list = []
thread_id_list = []

for user in username_list:
    user_id = client.user_id_from_username(user)
    users_id_list.append(user_id)

for user_id in users_id_list:
    # direct_messages = client.direct_thread_by_participants(user_ids=[user_id])
    # print(f'Direct Messages: {direct_messages}')    

    # target_url = direct_messages['thread']['items'][0]['xma_media_share'][0]['target_url']
    # print(f"Target URL: {target_url}")

    # caption_text = direct_messages['thread']['items'][0]['xma_media_share'][0]['title_text']
    # print(f"Caption Text: {caption_text}")

    # photo_url = client.media_oembed(url=target_url).dict()['thumbnail_url']
    # print(f"Photo URL: {photo_url}")

    # media_path = client.photo_download_by_url(url=photo_url, folder="images")
    # print(f'Media Path: {media_path}')

    # media = client.photo_upload(
    # path=media_path,
    # caption=caption_text)
    # print(media)

#####################################################################
    direct_messages = client.direct_thread_by_participants(user_ids=[user_id])
    print(f'Direct Messages: {direct_messages.messages}\n')    

    # video_caption_text = direct_messages['thread']['items'][0]['clip']['clip']['caption']['text'] # [0]['title_text']
    # print(f"Video Caption Text: {video_caption_text}\n")

    # image_url = direct_messages['thread']['items'][0]['clip']['clip']['image_versions2']['candidates'][0]['url']
    # print(f"Image URL: {image_url}\n")
    
    # target_url = direct_messages['thread']['items'][0]['clip']['clip']['video_versions'][0]['url']
    # print(f"Target URL: {target_url}\n")


    # media_pk = client.media_pk_from_url(url=target_url)

    # # upload video
    # video_url = client.media_info(media_pk).video_url
    # print(f"Video URL: {video_url}\n")

    # video_path = client.video_download_by_url(url=video_url, folder="videos")
    # print(f"Video URL: {video_path}\n")

    # video_upload = client.video_upload(
    #     path=video_path,
    #     caption=video_caption_text
    # )
    # print(f'Video Upload: {video_upload}\n')



    # upload album with caption

    # timer that refresh after 1 hour

    time.sleep(5)
        



# Get the media PK, caption, and thumbnail URL
# media_pk = client.media_pk_from_url(url="https://www.instagram.com/p/Czd2Z9AKDhw/")
# media_caption = client.media_info(media_pk).dict()['caption_text']
# print(media_caption)

# photo_url = client.media_oembed(url="https://www.instagram.com/p/Czd2Z9AKDhw/").dict()['thumbnail_url']
# media_path = client.photo_download_by_url(url=photo_url, folder="imgs/")
# print(media_path)

# Upload the photo and caption as post
# media = client.photo_upload(
#     path=media_path,
#     caption=media_caption)
# print(media)