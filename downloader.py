from pyrogram import Client

API_ID =31467688
API_HASH ="bef22288484ea5945d0f97a047a850f3"
BOT_TOKEN ="9093453421:AAEvVPY-KVI09lkdy5vweIzns_lq7qKSheE"
CHAT_ID =8988444025
CHAT_START_ID = 1 # your gallery channel starting image id
CHAT_END_ID = 1000 # your gallery channel ending image id
proxy = None # your proxy settings, can be None

app = Client("gallery_downloader", api_id=31467688, api_hash="bef22288484ea5945d0f97a047a850f3",
             bot_token="9093453421:AAEvVPY-KVI09lkdy5vweIzns_lq7qKSheE" proxy=proxy)


file_unique_ids = set()
file_ids = {}
message_ids = {}

async def download_all():
    async with app:
        for i in range(CHAT_START_ID, CHAT_END_ID, 200):
            photos = await app.get_messages(CHAT_ID, [j for j in range(i, i+200)])
            for photo in photos:
                if photo.photo is not None:
                    file_unique_id = photo.photo.file_unique_id
                    file_id = photo.photo.file_id
                    message_id = photo.id
                    if file_unique_id in file_unique_ids:
                        continue
                    file_unique_ids.add(file_unique_id)
                    file_ids[file_unique_id] = file_id
                    message_ids[file_unique_id] = message_id
        for file_unique_id in file_ids:
            await app.download_media(file_ids[file_unique_id], file_name=f'data/{message_ids[file_unique_id]}.jpg')

app.run(download_all())