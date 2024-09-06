from pyrogram import filters
from YMusic import app
from YMusic.misc import _boot_
from YMusic.utils.formaters import get_readable_time
import config
import time

PING_COMMAND = ["uptime"]
PREFIX = config.PREFIX


@app.on_message(filters.command(PING_COMMAND, PREFIX))
async def _ping(_, message):
    uptime = get_readable_time(int(time.time() - _boot_))
    await message.reply_text(f"Uptime: {uptime}")
