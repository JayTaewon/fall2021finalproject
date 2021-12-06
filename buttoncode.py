import requests

token = "OTE0MTgyNjQxODcwMzMxOTA0.Ya4cRw.7ejCGxJ4iBkYxeV1yWntseCoNwc"
channel_ds = 914183399139336215

def sendMessage(token, channel_id, message):   
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id) 
    data = {"content": message}
    header = {"authorization": token}
    

    r = requests.post(url, data=data, headers=header)
    print(r.status_code)

sendMessage("OTE0MTgyNjQxODcwMzMxOTA0.Ya4cRw.7ejCGxJ4iBkYxeV1yWntseCoNwc", 914183399139336215, "EMERGENCY MEETING CALLED: SENDING YOU TO MEETING TABLE")
