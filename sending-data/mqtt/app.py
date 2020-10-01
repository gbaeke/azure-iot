# install paho-mqtt with pip3
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

# use clean_session to establish a persistent session
client = mqtt.Client(client_id='myDevice', clean_session=True, userdata=None, transport='tcp')

# set event handlers
client.on_connect=on_connect
client.on_log=on_log
client.on_publish=on_publish

# set user name and password; token is set in config.py
# user name is FQDN/deviceId
client.username_pw_set("iothub-geba-s1.azure-devices.net/myDevice",config.token)

# you need to explicitly trust the trusted root - Baltimore CyberTrust Root
cert = os.getcwd() + "/iot-hub-cert.cer"
client.tls_set(cert, tls_version=2)

# connect to IoT Hub with MQTT on secure port 8883
client.connect("iothub-geba-s1.azure-devices.net", 8883)

# this is the body
message = {
    "temperature": 99.9
}

# IoT Hub does not support qos 2 (will close the connection)
# retain should be set to false; here set to true as an example; if set to true mqtt-retain=true is sent as a prop
client.publish("devices/myDevice/messages/events/", payload=json.dumps(message), qos=1, retain=True)

# loop forever which also will show connection retries and PINGs
client.loop_forever()
