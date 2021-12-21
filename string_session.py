print(
    "ㅤ\nㅤ\n\n\n\nㅤ\n 

╭━━━┳╮╱╱╭┳━━━╮╭╮╱╭╮╭━━╮╭━━━┳━━━━╮
┃╭━━┫╰╮╭╯┃╭━╮┃┃┃╱┃┃┃╭╮┃┃╭━╮┃╭╮╭╮┃
┃╰━━╋╮╰╯╭┫╰━━╮┃┃╱┃┃┃╰╯╰┫┃╱┃┣╯┃┃╰╯
┃╭━━╯╰╮╭╯╰━━╮┃┃┃╱┃┃┃╭━╮┃┃╱┃┃╱┃┃
┃╰━━┳╮┃┃╭┫╰━╯┣┫╰━╯┣┫╰━╯┃╰━╯┃╱┃┃
╰━━━┻╯╰╯╰┻━━━┻┻━━━┻┻━━━┻━━━╯╱╰╯
	"
)
print("\n\n\n\n\nHello sir!!, I'm Here To Help u to Generate Telethon String Session")
print("\n\nEAGLEYUVI SPAMUSERBOT")

print("\n\nProperly Fill APP_ID ,HASH and Number.\n")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as hehe:
	dcsession = hehe.session.save()
	dEAGLE = hehe.send_message(
	    "me",
	    f"`{dcsession}`\n\n**Your EAGLEYUVI SPAMUSERBOT String Session Here Sir😁😎😎\nClick on above Code to Copy it\n\nFor Support Join** @BLACK_MAFIA_OP_BOLTE"
	)

print("\n\n############################\n")
print(
    "check your Telegram Saved Messages For Ur New String String Session 😂😂 or see below. ")

print("\n############################\n")


print(f"{dcsession}")

Print(" ")
