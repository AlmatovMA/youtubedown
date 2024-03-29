from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("нужна помошь?",
            "команды: ",
            "/start - запуск бота!",
            "/help - помошь!",
            "/audio - это команда для скачивания видео и отправка вам аудио сообщением")
    
    await message.answer("\n".join(text))
