# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

import time
import os
import sys
import asyncio
from six.moves import input
import threading
from azure.iot.device.aio import IoTHubModuleClient
import json

# global counters
TEMPERATURE_THRESHOLD = 25
TWIN_CALLBACKS = 0
RECEIVED_MESSAGES = 0

async def main():
    try:
        if not sys.version >= "3.5.3":
            raise Exception( "The sample requires python 3.5.3+. Current version of Python: %s" % sys.version )
        print ( "IoT Hub Client for Python - Azure IoT Edge" )

        # The client object is used to interact with your Azure IoT hub.
        module_client = IoTHubModuleClient.create_from_edge_environment()

        # connect the client.
        await module_client.connect()

        async def message_handler(message):
            global RECEIVED_MESSAGES
            global TEMPERATURE_THRESHOLD
            
            if message.input_name == "input1":
                print ("Message received on input1")
                
                # retrieve message text
                message_text = message.data.decode('utf-8')
                
                # restrieve custom properaties
                custom_properties = message.custom_properties
                
                print ( "    Messages properties: %s" % custom_properties )
                
                # print total number of received messages
                RECEIVED_MESSAGES += 1
                print ( "    Total messages received: %d" % RECEIVED_MESSAGES )
                
                # convert message text to JSON
                data = json.loads(message_text)

                # only send the data to output1 if temperature is an alert & add MessageType property
                if "machine" in data and "temperature" in data["machine"] and data["machine"]["temperature"] > TEMPERATURE_THRESHOLD:
                    custom_properties["MessageType"] = "Alert"
                    print ( "Machine temperature %s exceeds threshold %s" % (data["machine"]["temperature"], TEMPERATURE_THRESHOLD))
                    await module_client.send_message_to_output(message, "output1")
            else:
                print("Unknown input")

        # twin_patch_listener is invoked when the module twin's desired properties are updated.
        # update TEMPERATURE_THRESHOLD based on desired property of the module twin
        async def twin_patch_handler(patch):
            global TWIN_CALLBACKS
            global TEMPERATURE_THRESHOLD
            print( "Data in patch: %s" % patch)
            if "TemperatureThreshold" in patch:
                TEMPERATURE_THRESHOLD = patch["TemperatureThreshold"]
            TWIN_CALLBACKS += 1
            print ( "Total calls confirmed: %d\n" % TWIN_CALLBACKS )


        # set the message handler on the client
        module_client.on_message_received = message_handler

        # set the desired props patch handler
        module_client.on_twin_desired_properties_patch_received = twin_patch_handler

       # loop forever
        while True:
            print ("Module is waiting for messages on input1")
            await asyncio.sleep(30)

        # Finally, disconnect
        await module_client.disconnect()

    except Exception as e:
        print ( "Unexpected error %s " % e )
        raise

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    