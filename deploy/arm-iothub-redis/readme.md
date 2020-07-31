# IoT Hub ARM Template

***Create resource group:***

az group create --name resource-group-name --location westeurope

***Deploy template:***

az group deployment create --name deployment-name --resource-group resource-group-name --template-file .\azuredeploy.json --parameters azuredeploy.parameters.json

***Remarks***

- deploys IOT Hub, Function App (+ app settings), Redis Cache, Storage Account (for the Function App)
- this sample can be used with an Azure Function, connected to the Event Hub of the IoT Hub, that forwards messages to a Redis Cache; a client application and socket.io server that reads from Redis Cache can be used to show the data