# Simple IoT Hub ARM Template

***Create resource group:***

az group create --name resource-group-name --location westeurope

***Deploy template:***

az group deployment create --name deployment-name --resource-group resource-group-name --template-file ./azuredeploy.json --parameters azuredeploy.parameters.json

***Remarks***

- simple deployment of an IoT Hub + full access policy + custom authorization policy with ServiceConnect
- full schema: https://docs.microsoft.com/en-us/azure/templates/microsoft.devices/2018-04-01/iothubs
- outputs EventHubEndpoint

Grab the output with Azure CLI:

az deployment group show \
  -g resource-group-name \
  -n deployment-name \
  --query properties.outputs.EventHubEndpoint.value
