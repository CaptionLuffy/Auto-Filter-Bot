from pyrogram import Client, filters, enums
from info import INDEX_CHANNELS, INDEX_EXTENSIONS
from database.ia_filterdb import save_file

media_filter = filters.document | filters.video


@Client.on_message(filters.chat(INDEX_CHANNELS) & media_filter)
async def media(bot, message):
    """Media Handler"""
    '''media = getattr(message, message.media.value, None)
    if (str(media.file_name).lower()).endswith(tuple(INDEX_EXTENSIONS)):
        media.caption = message.caption
        await save_file(media)'''
    
    media = getattr(message, message.media.value, None)
    if media.mime_type in ['video/mp4', 'video/x-matroska']:  # Non .mp4 and .mkv files are skipped
        media.file_type = message.media.value
        media.caption = message.caption
        await save_file(media)

