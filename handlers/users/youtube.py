import os
from aiogram import*
from data.config import *
from aiogram.dispatcher.filters.builtin import CommandStart
from pytube import*
from loader import *
from keyboards.inline import markups as nav

async def check_sub(channels, user_id):
    for channel in channels:
        chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
        if chat_member['status'] == 'left':
            return False
    return True

@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    if message.chat.type == 'private':
        if await check_sub(CHANNELS, message.from_user.id):
            await message.answer(f"Привет! {message.from_user.full_name}")
        else:
            await bot.send_message(message.from_user.id, NOT_SUB_MESSAGE, reply_markup=nav.showChannels() )


@dp.message_handler()
async def text_message(message:types.message):
    if message.chat.type == 'private':
        if await check_sub(CHANNELS, message.from_user.id):
            chat_id=message.chat.id
            url=message.text
            yt=YouTube(url)
            if message.text.startswith=='https://youtu.be/' or 'https://youtu.com/':
                await bot.send_message(chat_id,f'Ваше видео:  {yt.title}\n'
                                            f'Скачанное с канала: [{yt.author}]({yt.channel_url})')
                await download_youtube_video(url, message, bot)                
        else:
            await bot.send_message(message.from_user.id, NOT_SUB_MESSAGE, reply_markup=nav.showChannels() )


async def download_youtube_video(url,message,text):         #Процес загрузки видео 
    if message.chat.type == 'private':
            if await check_sub(CHANNELS, message.from_user.id):
                chat_id=message.chat.id
                url=message.text
                yt=YouTube(url)
                from io import BytesIO
                buffer= BytesIO()
                if yt.check_availability() is None:
                    audio = yt.streams.get_audio_only()
                    audio.stream_to_buffer(buffer=buffer)
                    buffer.seek(0)
                    filename = yt.title
                    await message.answer_audio(audio=buffer,caption=filename)
                else:
                    await message.answer('не удалось скачать через этот URL')
                ytt = yt.title
                ytt = ytt.replace("|", "-")
                ytt = ytt.replace("_", "-")
                ytt = ytt.replace("#", "-")
                stream = yt.streams.filter(progressive=True, file_extension="mp4")
                stream.get_highest_resolution().download(f'{chat_id}', f'{ytt}')
                with open(f"{chat_id}/{ytt}", 'rb') as video:
                    await bot.send_video(chat_id, video, caption=ytt)
                    os.remove(f"{chat_id}/{ytt}") 
            else:
                await bot.send_message(message.from_user.id, NOT_SUB_MESSAGE, reply_markup=nav.showChannels() )
                    

# async def get_audio(message:types.Message):
#     if message.chat.type == 'private':
#         link=message.text
#         from io import BytesIO
#         buffer= BytesIO()
#         url= YouTube(link)
#         if url.check_availability() is None:
#             audio = url.streams.get_audio_only()
#             audio.stream_to_buffer(buffer=buffer)
#             buffer.seek(0)
#             filename = url.title
#             await message.answer_audio(audio=buffer,caption=filename)
#         else:
#             await message.answer('не удалось скачать через этот URL')



@dp.callback_query_handler(text="subchanneldone")
async def subchanneldone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)

    if await check_sub(CHANNELS, message.from_user.id):
        await message.answer(f"Привет!, {message.from_user.full_name}", reply_markup=nav.profileKeybord)
    else:
        await bot.send_message(message.from_user.id, NOT_SUB_MESSAGE, reply_markup=nav.showChannels() )

# @dp.callback_query_handler(text="360")
# async def quality360(message: types.Message):
#     await bot.delete_message(message.from_user.id, message.message.message_id)
#     chat_id=message.chat.id
#     url=message.text
#     yt=YouTube(url)
#     if message.text.startswith=='https://youtu.be/' or 'https://youtu.com/':
#         await bot.send_message(chat_id,f'Ваше видео:  {yt.title}\n'
#                                             f'Скачанное с канала: [{yt.author}]({yt.channel_url})')
#         ytt = yt.title
#         ytt = ytt.replace("|", "-")
#         ytt = ytt.replace("_", "-")
#         ytt = ytt.replace("#", "-")
#         yt.streams.filter(progressive=True, file_extension='mp4',resolution="360p")
#         stream= yt.streams.get_by_itag(18)
#         stream.download(f'{message.chat.id}', f'{message.chat.id}_{ytt}')
#         with open(f"{message.chat.id}\{message.chat.id}_{ytt}", 'wb') as video:
#             await bot.send_video(message.chat.id, video, caption=ytt)
#             os.remove(f"{message.chat.id}\{message.chat.id}_{ytt}") 
    
    

    

# @dp.callback_query_handler(text="720")
# async def quality720(message: types.Message):
#     await bot.delete_message(message.from_user.id, message.message.message_id)
#     chat_id=message.chat.id
#     url=message.text
#     yt=YouTube(url)
#     if message.text.startswith=='https://youtu.be/' or 'https://youtu.com/':
#         ytt = yt.title
#         ytt = ytt.replace("|", "-")
#         ytt = ytt.replace("_", "-")
#         ytt = ytt.replace("#", "-")
#         yt.streams.filter(progressive=True, filse_extension='mp4',resolution="360p")
#         stream= yt.streams.get_by_itag(18)
#         stream.download(f'{message.chat.id}', f'{message.chat.id}_{ytt}')
#         with open(f"{message.chat.id}\{message.chat.id}_{ytt}", 'wb') as video:
#             await bot.send_video(message.chat.id, video, caption=ytt)
#             os.remove(f"{message.chat.id}\{message.chat.id}_{ytt}") 
    