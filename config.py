# Import the os module.
import os
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv

def grab_token():
    # Loads the .env file that resides on the same level as the script.
    load_dotenv()
    # Grab the API token from the .env file.
    discord_token = os.getenv(key="key")
    return discord_token

# Tu bom pol dal nek gigaspam
copypasta = "FREŠER FREŠER FREŠER FREŠER"

# Dict za bot responses
responses = {
    "vilec": "L+ratio",
    "frešer": "classic frešer W",
    "kodric": "Papa Tilen = my Human Overlord"
}