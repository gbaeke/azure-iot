RGNAME=rg-iot-storage
ACCOUNTNAME=gebaiotstorage
CONTAINER=iot

# create resource group
az group create -n $RGNAME  -l westeurope

# create storage account
az storage account create -n $ACCOUNTNAME -g rg-iot-storage

# get connection string
az storage account show-connection-string -n $ACCOUNTNAME --query connectionString

# create container
az storage container create --name $CONTAINER --account-name gebaiotstorage