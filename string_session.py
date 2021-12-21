print(
    "ㅤ\nㅤ\n\n\n\nㅤ\n┈┈┏━╮╭━┓┈╭━━━━━━╮\n┈┈┃┏┗┛┓┃╭┫EAGLEYUVI SPAMUSERBOT ┃\n┈┈╰┓▋▋┏╯╯╰━━━━━━╯\n┈╭━┻╮╲┗━━━━╮╭╮┈\n┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈┏━╮╭━┓┈╭━━━━━━╮\n┈┈┃┏┗┛┓┃╭┫EAGLEYUVI SPAMUSERBOT ┃\n┈┈╰┓▋▋┏╯╯╰━━━━━━╯\n┈╭━┻╮╲┗━━━━╮╭╮┈\n┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈┏━╮╭━┓┈╭━━━━━━╮\n┈┈┃┏┗┛┓┃╭┫EAGLEYUVI SPAMUSERBOT ┃\n┈┈╰┓▋▋┏╯╯╰━━━━━━╯\n┈╭━┻╮╲┗━━━━╮╭╮┈\n┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈┏━╮╭━┓┈╭━━━━━━╮\n┈┈┃┏┗┛┓┃╭┫EAGLEYUVI SPAMUSERBOT ┃\n┈┈╰┓▋▋┏╯╯╰━━━━━━╯\n┈╭━┻╮╲┗━━━━╮╭╮┈\n┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n┈┈┈┈┈┗┻┛┗┻┛┈┈"
)
print("\n\n\n\n\nABE GANDU SUNN TU STRING SESSION GENERATE KARNA KYA TU IDHAR UDHAR LADKI KO DEKH RAHA VO SETTING HAI HAMARI. ABE CHAL NA CREATE KAR STRING SESSION")
print("\n\nEAGLEYUVI SPAMUSERBOT ")

print("\n\nProperly Fill APP_ID ,HASH and Number.\n")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as hehe:
	dcsession = hehe.session.save()
	dEAGLE = hehe.send_message(
	    "me",
	    f"`{dcsession}`\n\n**Your EAGLEYUVI String Session Here Sir😁😎😎\nClick on above Code to Copy it\n\nFor Support Join** @BLACK_MAFIA_OP_BOLTE"
	)

print("\n\n############################\n")
print(
    "IDHAR KUCH NHI H BE GANDU SUNN TU APNE ACCOUNT KA SAVE MESSAGES OPEN KAR OR UDHAR JAA KAR DEKHLE STRING SESSION PADA HOGA 😂😂. ")

print("\n############################\n")


print(f"{dcsession}")

Print(" ")
