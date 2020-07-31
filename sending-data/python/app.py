import paho.mqtt.client as mqtt
import json
import time
import os
import config

# callbacks
def on_connect(client, userdata, flags, rc):
    print("connected...")

def on_log(client, userdata, level, buf):
  print("log: ",buf)

def on_publish(client,userdata,result):
    print("result ", result)
    pass

client = mqtt.Client(client_id='myDevice', clean_session=True, userdata=None, transport='tcp')
client.on_connect=on_connect
client.on_log=on_log
client.on_publish=on_publish

# set user name and password; token is set in config.py
client.username_pw_set("iothub-geba-s1.azure-devices.net/myDevice",config.token)

# client tls settings
cert = os.getcwd() + "/iot-hub-cert.cer"
client.tls_set(cert, tls_version=2)

# connect to MQTT server on secure port
client.connect("iothub-geba-s1.azure-devices.net", 8883)

message = {
    "temperature": 27.8
}

# IoT Hub does not support qos 2 (will close the connection)
# retain should be set to false; if set to true mqtt-retain=true is sent as a prop
client.publish("devices/myDevice/messages/events/", payload=json.dumps(message), qos=1, retain=True)

# although not strictly needed here, loop forever which also will show connection retries and PINGs
client.loop_forever()
