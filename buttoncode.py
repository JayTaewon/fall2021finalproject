import gpiozero import Button                                                     #imports the button library so the Raspberry Pi knows what to do with the button signal

import requests                                                                   #imports the requests library which is what allows me to send a message through discord via the RPi.

token = "OTE0MTgyNjQxODcwMzMxOTA0.Ya4cRw.7ejCGxJ4iBkYxeV1yWntseCoNwc"             #Discord token, this is what allows the message to be sent by "Me" and not just a random id.
channel_ds = 914183399139336215                                                   #Routing number so the function knows which discord channel to send the message to.

def sendMessage(token, channel_id, message):                                      #Creating the messaging function
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)    #server URL
    data = {"content": message}                                                   #Message content
    header = {"authorization": token}                                             #Authorizes the messages to send
    

    r = requests.post(url, data=data, headers=header)                             #Actual post
    print(r.status_code)                                                          #Only needed to see if code works without having discord on hand.

    
button = Button(10)                                                               #This indicates which pin on the RPi that the button is connected to
button.wait_for_press()                                                           #This is what arms the button, and then it waits for a signal from the pressed button to execute the next line.

sendMessage("OTE0MTgyNjQxODcwMzMxOTA0.Ya4cRw.7ejCGxJ4iBkYxeV1yWntseCoNwc", 914183399139336215, "EMERGENCY MEETING CALLED: SENDING YOU TO MEETING TABLE") 
