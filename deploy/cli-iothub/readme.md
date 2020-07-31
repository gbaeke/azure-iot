# Use Azure CLI to deploy IoT Hub

### Resource Group

az group create --name resource-group-name --location westeurope

Unsure about locations?

az account list-locations -o table

### IoT Hub

az iot hub create --name IoTHub-name \
   --resource-group resource-group-name --sku S1 --unit 2

az iot hub list -o table


### Use the Azure IoT Extension for more options

az extension add --name azure-iot

More info: https://github.com/Azure/azure-iot-cli-extension

Now run:

az iot hub -h

This added functionality like: device, dps, edge and more...

For example, to create a device:

az iot hub device-identity create --device-id testdevice --hub-name IoTHub-name

To list devices:

az iot hub device-identity list --hub-name iothub-geba-s1

### If you use VS Code

Get the IoT Hub extension via the extension pack: https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-tools

The pack contains tools for:

- IoT Hub
- IoT Edge
- Device Workbench: to write device software




