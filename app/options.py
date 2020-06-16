import requests
import os
import json
from dotenv import load_dotenv

# Create secret api key from env variable:
load_dotenv()
key = os.getenv("OPTIONS_KEY")

# Construct request based on user input:
quote = input("Please submit stock quote: ")

url = "https://stock-and-options-trading-data-provider.p.rapidapi.com/options/" + quote

headers = {
    'x-rapidapi-host': "stock-and-options-trading-data-provider.p.rapidapi.com",
    'x-rapidapi-key': key,
    'x-rapidapi-proxy-secret': "a755b180-f5a9-11e9-9f69-7bf51e845926"
    }

response = requests.request("GET", url, headers=headers)
parsed_response = json.loads(response.text)
breakpoint()
# Export information to data file