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
    "bitches": "Looking for a female roomate to pay $0 rent I will not charge you money, but I will be sharing my bed with you as the other room is being used by my parents. They are aware of this arrangement as I have done this before but it has not worked out for reasons rather not say on here. I will expect hugs at least 5 times a day, and cuddles at least 2 times a day for at least 10 minutes each. You will not be dating any other man during this arrangement, you will have no male friends either. You may have female friends and they may visit if they like. You will also be required to make me meals 3 times a day. Physical requirements are as stated: Must be shorter than 5'5, weigh no more than 120 Ibs, caucasian or asian only, republican, biologically female, no tattoos, no Muslims, no vegans, no smoking/ vaping, marywania, and you MUST shave legs and underarms. I am 44-male/290 Ibs last time I checked, 5'6. Please contact me if you would like this arrangement."
}

bot_ids = {"736888501026422855", "184405311681986560", "432610292342587392"}

# Champ array
with open('champs.txt') as f:
    champs = [champ.rstrip('\n') for champ in f]
