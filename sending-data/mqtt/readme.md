# MQTT to IoT Hub with Python

The code has been tested with Python 3.8.5 64-bit. Python interpreter in these docs is **python3.8** as installed via PPA - https://tech.serhatteker.com/post/2019-12/how-to-install-python38-on-ubuntu/

## app.py

Uses the PAHO MQTT client. Install with:

pip3 install paho-mqtt

(More info about package: https://pypi.org/project/paho-mqtt/)

*Note:* if you have multiple versions of Python installed and you have a mismatch between pip3 and python3, you can run pip3 with your Python version. For instance, when python3.8 is installed, you could use **python3.8 $(which pip3) install paho-mqtt**

Before running app.py, add a **config.py** file that has a string variable called **token**. Set token to the value of the SharedAccessSignature (SAS). Make sure you generate a valid SAS with VSCode.

With the PAHO MQTT library installed and config.py created, run **python3.8 app.py* or **python3 app.py**

The result should be:

log:  Sending CONNECT (u1, p1, wr0, wq0, wf0, c1, k60) client_id=b'myDevice'
log:  Sending PUBLISH (d0, q1, r1, m1), 'b'devices/myDevice/messages/events/'', ... (21 bytes)
log:  Received CONNACK (0, 0)
connected...
log:  Received PUBACK (Mid: 1)
result  1

If the SAS is invalid, you will see the PAHO client trying to send the message multiple times.

## app-sas.py

This script generates the SAS token on the fly. It needs the **symmetric key** in order to create the token. Set a string variable called **key** in config.py:

key="YOUR KEY HERE"

The script uses the PAHO MQTT client as well.