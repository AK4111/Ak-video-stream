# Copyright (C) 2021 By VeezMusicProject

from driver.core import me_bot
from driver.decorators import check_blacklist
from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup, stream_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("home start")
    await query.edit_message_text(
        f"""โจ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Is a bot to play music and video in groups, through the Telegram Group video chat!**

๐ก **Find out all the Bot's commands and how they work by clicking on the ยป ๐ Commands button!**

๐ **To know how to use this bot, please click on the ยป โ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ Add me to your Group โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โ Basic Guide", callback_data="user_guide")],
                [
                    InlineKeyboardButton("๐ Commands", callback_data="command_list"),
                    InlineKeyboardButton("โค Donate", url=f"https://t.me/{OWNER_USERNAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ Source Code", url="https://github.com/levina-lab/video-stream"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""โน๏ธ Quick use Guide bot, please read fully !

๐ฉ๐ปโ๐ผ ยป /play - Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

๐ฉ๐ปโ๐ผ ยป /vplay - Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

๐ฉ๐ปโ๐ผ ยป /vstream - Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

โ Have questions? Contact us in [Support Group](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="user_guide")]]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    ass_uname = me_bot.first_name
    await query.answer("user guide")
    await query.edit_message_text(
        f"""โ How to use this Bot ?, read the Guide below !

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{ass_uname} to your group or type /userbotjoin to invite her, unfortunately the userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`.
4.) Turn on/Start the video chat first before start to play video/music.

`- END, EVERYTHING HAS BEEN SETUP -`

๐ If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

๐ก If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ยป Quick use Guide ยซ", callback_data="quick_use")
                ],[
                    InlineKeyboardButton("๐ Go Back", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป Check out the menu below to read the module information & see the list of available Commands !

All commands can be used with (`! / .`) handler""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ฎ๐ปโโ๏ธ Admins Commands", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("๐ฉ๐ปโ๐ผ Users Commands", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("Sudo Commands", callback_data="sudo_command"),
                    InlineKeyboardButton("Owner Commands", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("๐ Go Back", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""โ๏ธ Command list for all user.

ยป /play (song name/link) - play music on video chat
ยป /vplay (video name/link) - play video on video chat
ยป /vstream (m3u8/yt live link) - play live stream video
ยป /playlist - see the current playing song
ยป /lyric (query) - scrap the song lyric
ยป /video (query) - download video from youtube
ยป /song (query) - download song from youtube
ยป /search (query) - search a youtube video link
ยป /ping - show the bot ping status
ยป /uptime - show the bot uptime status
ยป /alive - show the bot alive info (in Group only)

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""โ๏ธ Command list for group admin.

ยป /pause - pause the current track being played
ยป /resume - play the previously paused track
ยป /skip - goes to the next track
ยป /stop - stop playback of the track and clears the queue
ยป /vmute - mute the streamer userbot on group call
ยป /vunmute - unmute the streamer userbot on group call
ยป /volume `1-200` - adjust the volume of music (userbot must be admin)
ยป /reload - reload bot and refresh the admin data
ยป /userbotjoin - invite the userbot to join group
ยป /userbotleave - order userbot to leave from group
ยป /startvc - start/restart the group call
ยป /stopvc - stop/discard the group call

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in SUDO_USERS:
        await query.answer("โ?๏ธ You don't have permissions to click this button\n\nยป This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""โ๏ธ Command list for sudo user.

ยป /stats - get the bot current statistic
ยป /calls - show you the list of all active group call in database
ยป /block (`chat_id`) - use this to blacklist any group from using your bot
ยป /unblock (`chat_id`) - use this to whitelist any group from using your bot
ยป /blocklist - show you the list of all blacklisted chat
ยป /speedtest - run the bot server speedtest
ยป /sysinfo - show the system information
ยป /eval - execute any code (`developer stuff`)
ยป /sh - run any command (`developer stuff`)

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in OWNER_ID:
        await query.answer("โ?๏ธ You don't have permissions to click this button\n\nยป This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""โ๏ธ Command list for bot owner.

ยป /gban (`username` or `user_id`) - for global banned people, can be used only in group
ยป /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
ยป /update - update your bot to latest version
ยป /restart - restart your bot directly
ยป /leaveall - order userbot to leave from all group
ยป /leavebot (`chat id`) - order bot to leave from the group you specify
ยป /broadcast (`message`) - send a broadcast message to all groups in bot database
ยป /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("โ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
