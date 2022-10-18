# Import the os module.
import os
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
import pandas as pd

def grab_token():
    # Loads the .env file that resides on the same level as the script.
    load_dotenv()
    # Grab the API token from the .env file.
    discord_token = os.getenv("key")
    return discord_token

# Tu bom pol dal nek gigaspam
copypastas = "FREŠER FREŠER FREŠER FREŠER"

# Dict za bot responses
responses = {
    "vilec": "L+ratio",
    "frešer": "classic frešer W",
    "kodric": "Papa Tilen = my Human Overlord",
    "bitches": "Looking for a female roomate to pay $0 rent I will not charge you money, but I will be sharing my bed with you as the other room is being used by my parents. They are aware of this arrangement as I have done this before but it has not worked out for reasons rather not say on here. I will expect hugs at least 5 times a day, and cuddles at least 2 times a day for at least 10 minutes each. You will not be dating any other man during this arrangement, you will have no male friends either. You may have female friends and they may visit if they like. You will also be required to make me meals 3 times a day. Physical requirements are as stated: Must be shorter than 5'5, weigh no more than 120 Ibs, caucasian or asian only, republican, biologically female, no tattoos, no Muslims, no vegans, no smoking/ vaping, marywania, and you MUST shave legs and underarms. I am 44-male/290 Ibs last time I checked, 5'6. Please contact me if you would like this arrangement.",
    "lukas": "Maybe if you got rid of that old yee-yee ass haircut you'd get some bitches on yo dick. Oh, better yet maybe Tanisha'll call your dog ass if she stop fucking with that brain surgeon or lawyer she fucking with. Nigga.",
    "vilec moto": "SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD SEX BAD GARLIC BREAD GOOD ",
    "oktober": "BOO!! Sorry did I scare you?! WASSUP GURL😉😉😊 ITS COCKTOBER 😈🌚🍂🍃🍁 AND IF YOU👈🏽 ARE GETTING THIS👇🏽😘 IT MEANS UR A HALLOWEEN 👻🎃 HOE😏😩👅💦 every year in Cocktober the jack o slut🎃 comes to life🙀😻🙌🏽👏👏🙌🏽 coming to harvest 🍁🍂🍃 his hoes for THOT-O-WEEN😏😏💥💥🎈🎂🎉 send this to 10 other Halloween Hoes or else you a TRICK🎃👻👻 🎃 IF YOU GET 4 BACK UR A THOT-O-WEEN TREAT😋 IF YOU GET 6 BACK UR A SLUTTY WITCH BITCH👄😍✨🔮 BUT IF YOU GET 10 BACK UR THE SPOOKIEST SLUT ON THE BLOCK😜💦⚰🎉🎉💯🎃 If you don’t send this to 1️⃣0️⃣other thots💁😩👄 you will get NO DICK 👋 this COCKTOBER🎃😉😜",
    "vape": "HEY YOU!!! 😉 HEY SWEETIE😻 🎂🎂😊YOU GOT WHAT I NEED 👅😳🥴😈 I am offering you THE 🍁 👄👈🏽🍁 CHANCE TO🙌🏽 JOIN MY UNDERGROUND😩😻😻👋😩 SEX RING👈🏽 😩 😩 😉 THE🙀 😂😉👻 WINNER TAKES IT ALL🙀⚡💡🔥😵 so you NEED 🌚 to see this 😘 👹🎃🫶😼TAKE THIS OFFER😊 SO THAT YOU🎃 CAN FIND OUT HOW SLUTTY 😘 YOU REALLY ARE💯 💥 MEET ME AT THE BACK OF CLOUD 9️⃣ VAPE🚬🚬🚬🚬😽😽 SHOP SHOP SO WE CAN🎈 ⚰️ 💦 💦 TAKE THIS 🎂 BITCH FOR A SPIN💦 ⚰️ WHAT CAN DAT ASS DO????? 🔮 🔮 🔮 SEND THIS TO 1️⃣ 0️⃣ 0️⃣ OTHER SLUTTY👯‍♀️✨✨ 🍃 SINGLES SO✨ WE CAN 😻 RLLY HAVE SOME FUN✨😋IF YOU DONT SEND THIS TO 1️⃣0️⃣0️⃣ OTHER SLUTTY SLIDERS YOUR FATHER WILL BUILD AN UNDERGROUND METHLAB👨‍🦲🔭🧪🔬 BUT IF YOU SEND THIS TO 1️⃣0️⃣0️⃣ SLIPPIN SLUTS🗾💁🎈 YOULL GET SOME GOOD 🇵🇺🇸🇸SS🇾 TONIGHT😘😘😜😜😈"
}

bot_ids = {"736888501026422855", "184405311681986560", "432610292342587392"}

# Champ array
with open('champs.txt') as f:
    champs = [champ.rstrip('\n') for champ in f]
