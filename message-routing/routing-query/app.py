# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os
import asyncio
import uuid
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import config
import random
import time
import datetime
import json

async def main():
    # get connection string from config.py (not stored in git)
    conn_str = config.connstr

    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the client.
    await device_client.connect()

    async def send_message(temperature):
        print("sending message with temperature " + str(temperature))

        body = {
            "time": str(datetime.datetime.utcnow()),
            "temperature": temperature,
            "deviceId": "myDevice"
        }

        

        msg = Message(json.dumps(body))

        # message-id is a user-settable identifier for the message
        msg.message_id = uuid.uuid4()

        # custom_properties is a dictionary of application properaties
        if temperature > 25:
            msg.custom_properties["alert"] = "too hot"
            print("we sent an alert")

        # json format
        msg.content_encoding = "UTF-8"
        msg.content_type = "application/json"

        # send the message and wait until sent
        await device_client.send_message(msg)
        print("done sending message")

    # send `messages_to_send` messages in parallel
    while True:
        temperature = 20 + random.random() * 10
        await send_message(temperature)
        time.sleep(1)


if __name__ == "__main__":
    #asyncio.run(main())

    # If using Python 3.6 or below, use the following code instead of asyncio.run(main()):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()