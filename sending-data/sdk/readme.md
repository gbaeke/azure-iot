### SDK Sample

Note: skd.py uses the V2 API (see https://github.com/Azure/azure-iot-sdk-python)

If you use the ***generate code*** option in VS Code, the V1 SDK is used. On Ubuntu 18.04 with Python 3.6.9, that code does not run due to dependency issues. V1 is deprecated.

The Python SDK only supports MQTT (on 31/7/2020)

- supports symmetric key auth and X-509
- device to cloud with optional properties
- receive C2D messages
- ...

To run sdk.py, install the azure-iot-device library. See https://pypi.org/project/azure-iot-device/. Install with:

pip3 install azure-iot-device


The Azure IoT SDK for Python supports the use of connection strings for a device. You can get the connection string from VS Code by right clicking the device and clicking **Copy Device Connection String**. Add the connection string to a **connstr** variable in **config.py**

The scripts sends 100 messages. This is configurable.