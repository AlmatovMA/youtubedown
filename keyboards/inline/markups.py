from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from data.config import CHANNELS


def showChannels():
    keybord = InlineKeyboardMarkup(row_width=1)

    for channel in CHANNELS:
        btn = InlineKeyboardButton(text=channel[0], url=channel[2])
        keybord.insert(btn)

    btnDoneSub = InlineKeyboardButton(text="Я ПОДПИСАЛСЯ", callback_data="subchanneldone")
    keybord.insert(btnDoneSub)
    return keybord

def showQuality():
    keybord = InlineKeyboardMarkup(row_width=2)
    btn360 = InlineKeyboardButton(text="360", callback_data="360")
    btn720 = InlineKeyboardButton(text="720", callback_data="720")
    keybord.add(btn360,btn720)
    return keybord