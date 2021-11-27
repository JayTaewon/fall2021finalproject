import requests

# https://discord.com/api/v9/channels/914183399139336215/messages

payload = {
    'content': "Hello World"
}

header = {
    'authorization': 'OTE0MTgyNjQxODcwMzMxOTA0.YaJWDA.UdJHuHMKBx0IUElSaXEFSxNpeMk'
}

r = requests.post("https://discord.com/api/v9/channels/914183399139336215/messages", data=payload, headers=header)
