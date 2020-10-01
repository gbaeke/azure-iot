import os

# SDK makes heavy use of asyncio
import asyncio
import uuid
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import config

messages_to_send = 100


async def main():
    # get connection string from config.py (not stored in git)
    conn_str = config.connstr

    # The client object is used to interact with your Azure IoT hub.
    # No need to generate SAS token as this is hidden by the SDK
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the client.
    await device_client.connect()

    async def send_test_message(i):
        print("sending message #" + str(i))

        # Message is part of the SDK
        msg = Message("test wind speed " + str(i))
        
        # Message objects support additional properties
        msg.message_id = uuid.uuid4()
        
        # You can set custom properties, different from the actual payload
        msg.custom_properties["tornado-warning"] = "yes"

        await device_client.send_message(msg)
        print("done sending message #" + str(i))

    # send `messages_to_send` messages in parallel
    await asyncio.gather(*[send_test_message(i) for i in range(1, messages_to_send + 1)])

    # finally, disconnect
    await device_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

    # If using Python 3.6 or below, use the following code instead of asyncio.run(main()):
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop.close()