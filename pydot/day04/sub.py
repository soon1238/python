import paho.mqtt.client as mqtt
from slackclient import SlackClient

def sendMessageToSlack(msg):
    slack_token="xoxb-259967078277-O0ZnHWiXcTi8t4tctwcVV8cY"
    sc=SlackClient(slack_token)
    resp=sc.api_call("chat.postMessage",channel= "#saviour",text=msg)

def on_connect(client,userdata,flags,rc):
    print("Connected with result code"+str(rc))
    client.subscribe("saviour")

def on_message(client,userdata,msg):
    print msg
    decoded_msg=msg.payload.decode()
    print (decoded_msg)
    # if decoded_msg=="":
    #     print("Yes!")
    sendMessageToSlack(decoded_msg)
    #client.disconnect()

client=mqtt.Client()
client.connect("10.20.10.106",7000,60)

client.on_connect=on_connect
client.on_message=on_message

client.loop_forever()
