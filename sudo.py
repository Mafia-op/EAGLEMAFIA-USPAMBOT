import os

 

import heroku3

from telethon.tl.functions.users import GetFullUserRequest

 

 

 

 

@bot.on((outgoing=True, pattern="sudo(?: |$)(.*)"))

async def sudo(event):

    sudo = "True" if SUDO_USERS else "False"

    users = sudousers

    if sudo == "True":

        await event.edit(

            f"🔮 Sudo: Enabled\n\n📚  List Sudo Users:\n» {users}\n\nSUDO_HANDLER: {SUDO_HANDLER}",

        )

    else:

        await edit_delete(event, "🔮 Sudo: Disabled")

 

 

@bot.on(outgoing=True, pattern="addsudo(?: |$)(.*)"))

async def add(event):

    suu = event.text[9:]

    if f"{cmd}add " in event.text:

        return

    if event.sender_id in SUDO_USERS:

        return

    event = await event.edit("Processing...")

    var = SUDO_USERS

    reply = await event.get_reply_message()

    if not suu and not reply:

        return await edit_delete(

            event,

      "Reply to the user or provide a user id to add him to your sudo user list.",

            45,

        )

    if suu and not suu.isnumeric():

        return await edit_delete(

            event, "Berikan User ID atau reply ke pesan penggunanya.", 45

        )

    if HEROKU_APP_NAME is not None:

        app = Heroku.app(HEROKU_APP_NAME)

    else:

        await edit_delete(

            event,

"Please Add Var HEROKU_APP_NAME to add sudo user",

)       

 return

    heroku_Config = app.config()

    if event is None:

        return

    if suu:

        target = suu

    elif reply:

        target = await get_user(event)

    suudo = f"{sudousers} {target}"

    newsudo = suudo.replace("{", "")

    newsudo = newsudo.replace("}", "")

    await event.edit(

   f"Successfully Added {target} to sudo User.\n\nRestarting Heroku to Apply Changes."

    )

    heroku_Config[var] = newsudo

 

 

@bot.on((outgoing=True, pattern="delsudo(?: |$)(.*)"))

async def _(event):

    if event.sender_id in SUDO_USERS:

        return

    suu = event.text[8:]

    event = await event.edit("Processing...")

    reply = await event.get_reply_message()

    if not suu and not reply:

        return await edit_delete(

            event,

      "Reply to user or provide user id to remove it from your sudo user list.",

45,

)

    if suu and not suu.isnumeric():

        return await edit_delete(

            event, " Provide User ID or reply to user messages.", 45

        )

    if HEROKU_APP_NAME is not None:

        app = Heroku.app(HEROKU_APP_NAME)

    else:

        await edit_delete(

            event,

          "Please Add Var HEROKU_APP_NAME to delete sudo user",

)

        return

    heroku_Config = app.config()

    if event is None:

        return

    if suu != "" and suu.isnumeric():

        target = suu

    elif reply:

        target = await get_user(event)

    gett = str(target)

    if gett in sudousers:

        newsudo = sudousers.replace(gett, "")

        await event.edit(

         f"Successfully Removed {target} from User sudo.**\n\nRestarting Heroku to Apply Changes."

        )

        var = "SUDO_USERS"

        heroku_Config[var] = newsudo

    else:

        await edit_delete(

            event, " This user is not in your sudo User List.", 45

)

 

 

async def get_user(event):

    if event.reply_to_msg_id:

        previous_message = await event.get_reply_message()

        if previous_message.forward:

            replied_user = await event.client(

                GetFullUserRequest(previous_message.forward.sender_id)

            )

        else:

            replied_user = await event.client(

                GetFullUserRequest(previous_message.sender_id)

            )

    return replied_user.user.id
