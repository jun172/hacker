import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("broker.hivemq.com",1883,60)

client.publish("iot/sensor/temp","25.6")
client.disconnect()