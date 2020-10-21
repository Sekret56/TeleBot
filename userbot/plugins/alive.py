# For @TeleBotHelp
"""DarkUserBot-un Çalışdığını Yoxlayın."""
import os
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME, telever
from userbot.__init__ import StartTime
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd, sudo_cmd

ALV_PIC = os.environ.get("ALIVE_PIC", None)

if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@DarkSupportGroup"


@telebot.on(admin_cmd(outgoing=True, pattern="alive"))
@telebot.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ Botunuzun çalışdığını yoxlamaq üçün .alive əmrindən istifdə edin.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        tele = "➥ **DARK USER BOT:** `ƏLA İŞLƏYİR`\n\n"
        tele += "➥ **SİSTEM HAQQINDA**\n"
        tele += "`➥ **Telethon Versiya:`** `1.17` \n" **Python:** `3.8.5` \n"
        tele += f"`➥ **Dark Versiya** :` **{telever}**\n"
        tele += f"`➥ **Son Güncəlləmə** :` **{uptime}**\n"
        tele += "`➥ **Database Status**:` **Hərşey Əladı 👌**\n"
        tele += f"`➥ **Sahibim** :` {DEFAULTUSER} \n"
        tele += "➥ **Lisenziya** : GNU General Public License v3.0\n"
        tele += "    **🇦🇿DARK USER BOT🇦🇿**"

        await alive.get_chat()
        await alive.delete()
        """ Botunuzun çalışdığını yoxlamaq üçün .alive əmrindən istifdə edin.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=tele, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://i.imgur.com/uDZZsHQ.gif")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "dark.webp"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            "➥ **DARK USER BOT:** `ƏLA İŞLƏYİR`\n\n"
            "➥ **SİSTEM HAQQINDA**\n"
            "`➥ **Telethon Versiya:`** `1.17` \n" **Python:** `3.8.5` \n"
            f"`➥ **Dark Versiya** :` **{telever}**\n"
            f"`➥ **Son Güncəlləmə** :` **{uptime}**\n"
            "`➥ **Database Status**:` **Hərşey Əladı 👌**\n"
            f"`➥ **Sahibim** :` {DEFAULTUSER} \n"
            "`➥ **Lisenziya** :` GNU General Public License v3.0\n"
            "    **🇦🇿DARK USER BOT🇦🇿**"
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()
