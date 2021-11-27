import requests

# https://discord.com/api/v9/channels/914183399139336215/messages
# https://discord.com/api/v9/channels/914183399139336215/messages

# content: "pretty cool"
# authorization: OTE0MTgyNjQxODcwMzMxOTA0.YaJijw.eWBxxSa11GYNJAsnG20NGgv556A

# Note to self: Discord must be signed in on the RPi for this to work.

payload = {
    'content': "DISCORD IS CLOSED AND IS WORKING WHAT DID I DO"
}

header = {
    'authorization': 'OTE0MTgyNjQxODcwMzMxOTA0.YaJijw.eWBxxSa11GYNJAsnG20NGgv556A'
}

r = requests.post("https://discord.com/api/v9/channels/914183399139336215/messages", data=payload, headers=header)
