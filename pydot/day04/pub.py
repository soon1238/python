import paho.mqtt.client as mqtt
client=mqtt.Client()
client .connect("10.20.10.106",7000,60)
client.publish("bot","soon")
client.disconnect()
