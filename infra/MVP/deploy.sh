#!/bin/bash

# Deployment settings
RESOURCE_GROUP="rg-atheryon-cdm-core-prod-aue"
LOCATION="australiaeast"
SQL_ADMIN_USER="cdmadmin"

echo "🔐 Enter SQL Admin Password (for Azure SQL):"
read -s SQL_ADMIN_PASSWORD

echo "✅ Creating resource group: $RESOURCE_GROUP"
az group create \
  --name "$RESOURCE_GROUP" \
  --location "$LOCATION"

echo "🚀 Deploying Bicep template to $RESOURCE_GROUP..."
az deployment group create \
  --resource-group "$RESOURCE_GROUP" \
  --template-file main.bicep \
  --parameters sqlAdminPassword="$SQL_ADMIN_PASSWORD"

echo "🎉 Deployment complete!"
