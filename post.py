from instagrapi import Client
from instagrapi.types import Usertag
import time

# Replace 'your_username' and 'your_password' with your Instagram credentials
username = 'omarelsherif0102'
password = 'Collegeboard@010'

# Create an instance of the Client
client = Client()
client.login(username, password)

username_list = ["danilgreen","polianskiyartem"]
users_id_list = []
Messages = {'media_link':[],
           'video_media_pk': []}


for user in username_list:
    user_id = client.user_id_from_username(user)
    users_id_list.append(user_id)

for user_id in users_id_list:    
    direct_messages = client.direct_thread_by_participants(user_ids=[user_id])
    # print(f'Direct Messages: {direct_messages}\n')

    ### Photo and Album
    if direct_messages["thread"]["items"][0]["item_type"] == "xma_media_share":
        print(f"Item Type: {direct_messages['thread']['items'][0]['item_type']}\n")
        print(f"Media Share: {direct_messages['thread']['items'][0]['xma_media_share']}\n")

        ## Get the media PK, caption, and thumbnail URL
        media_link = direct_messages['thread']['items'][0]['xma_media_share'][0]['target_url']
        print(f"Media Link: {media_link}\n")
        if media_link not in Messages['media_link']:
            Messages['media_link'].append(media_link)

            media_url = media_link[:40]
            media_pk = client.media_pk_from_url(url=media_url)
            media_caption = client.media_info(media_pk).dict()['caption_text']
            # print(media_caption)
            
            media_path = client.album_download(media_pk=media_pk, folder="albums")
            # print(f'Media Path: {media_path}\n')

            # Upload the album and caption as post
            media = client.album_upload(
                paths=media_path,
                caption=media_caption)
            # print(media)


    ### Video Message
    elif direct_messages["thread"]["items"][0]["item_type"] == "clip":
        # print(f"Item Type: {direct_messages['thread']['items'][0]['item_type']}\n")
        # print(f"Clip: {direct_messages['thread']['items'][0]['clip']}\n")

        video_media_pk = direct_messages['thread']['items'][0]['clip']['clip']['pk']

        if video_media_pk not in Messages['video_media_pk']:
            Messages['video_media_pk'].append(video_media_pk)

            media_caption = client.media_info(video_media_pk).dict()['caption_text']
            # print(media_caption)

            video_url = client.media_info(video_media_pk).dict()['video_url']
            # print(f'Video URL: {video_url}\n')

            media_path = client.video_download_by_url(url=video_url, folder="videos")
            # print(f"Media Path: {media_path}\n") 

            # Upload the video and caption as post
            media = client.video_upload(
                path=media_path,
                caption='video message upload test')
            # print(media)

    sleep_time_in_seconds = 1 * 30 * 60
    time.sleep(sleep_time_in_seconds)


    # target_url = direct_messages['thread']['items'][0]['xma_media_share'][0]['target_url']
    # print(f"Target URL: {target_url}\n")

    # caption_text = direct_messages['thread']['items'][0]['xma_media_share'][0]['title_text']
    # print(f"Caption Text: {caption_text}\n")

    # photo_url = client.media_oembed(url=target_url).dict()['thumbnail_url']
    # print(f"Photo URL: {photo_url}")

    # media_path = client.photo_download_by_url(url=photo_url, folder="images")
    # print(f'Media Path: {media_path}')

    # media = client.photo_upload(
    # path=media_path,
    # caption=caption_text)
    # print(media)

# #####################################################################
#     direct_messages = client.direct_thread_by_participants(user_ids=[user_id])
#     print(f'Direct Messages: {direct_messages}\n')    

    # video_caption_text = direct_messages['thread']['items'][0]['clip']['clip']['caption']['text'] # [0]['title_text']
    # print(f"Video Caption Text: {video_caption_text}\n")

    # image_url = direct_messages['thread']['items'][0]['clip']['clip']['image_versions2']['candidates'][0]['url']
    # print(f"Image URL: {image_url}\n")
    
    # target_url = direct_messages['thread']['items'][0]['clip']['clip']['video_versions'][0]['url']
    # print(f"Target URL: {target_url}\n")


    # media_pk = client.media_pk_from_url(url=target_url)

    # # upload video
   


    # upload album with caption

    # timer that refresh after 1 hour

    # time.sleep(5)
        



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



 #### Video Download and Upload Correctly
# Get the media PK, caption, and thumbnail URL
# media_pk = client.media_pk_from_url(url="https://www.instagram.com/p/CzjN3jNtT6s/")
# media_caption = client.media_info(media_pk).dict()['caption_text']
# # print(media_caption)

# video_url = client.media_info(media_pk).dict()['video_url']
# print(f'Video URL: {video_url}\n')
# media_path = client.video_download_by_url(url=video_url, folder="videos")
# print(media_path)

# # Upload the video and caption as post
# media = client.video_upload(
#     path=media_path,
#     caption='video upload test')
# print(media)

# ### album download and upload Correctly  
# # Get the media PK, caption, and thumbnail URL
# media_pk = client.media_pk_from_url(url="https://www.instagram.com/p/CzvDPDaNFgJ/")
# # media_caption = client.media_info(media_pk).dict()['caption_text']
# # print(media_caption)

# # video_url = client.media_info(media_pk).dict()['video_url']
# # print(f'Video URL: {video_url}\n')
# media_path = client.album_download(media_pk=media_pk, folder="albums")
# print(f'Media Path: {media_path}\n')

# # Upload the album and caption as post
# media = client.album_upload(
#     paths=media_path,
#     caption='album upload test')
# print(media)
