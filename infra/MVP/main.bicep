param location string = resourceGroup().location
param sqlAdminUser string = 'cdmadmin'
@secure()
param sqlAdminPassword string

var storageAccountName = 'cdmstorage${uniqueString(resourceGroup().id)}'
var sqlServerName = 'cdmsql${uniqueString(resourceGroup().id)}'
var functionAppName = 'cdmfunction${uniqueString(resourceGroup().id)}'
var appServicePlanName = 'cdmAppPlan'
var webAppName = 'cdmwebapp${uniqueString(resourceGroup().id)}'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'cdm-insights'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
  }
}

resource hostingPlan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: 'Y1'
    tier: 'Dynamic'
  }
  kind: 'functionapp'
}

resource functionApp 'Microsoft.Web/sites@2022-09-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp'
  properties: {
    serverFarmId: hostingPlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'AzureWebJobsStorage'
          value: storageAccount.properties.primaryEndpoints.blob
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'python'
        }
        {
          name: 'APPINSIGHTS_INSTRUMENTATIONKEY'
          value: appInsights.properties.InstrumentationKey
        }
      ]
    }
  }
  dependsOn: [
    hostingPlan
    storageAccount
    appInsights
  ]
}

resource sqlServer 'Microsoft.Sql/servers@2022-11-01-preview' = {
  name: sqlServerName
  location: location
  properties: {
    administratorLogin: sqlAdminUser
    administratorLoginPassword: sqlAdminPassword
  }
}

resource sqlDatabase 'Microsoft.Sql/servers/databases@2022-11-01-preview' = {
  parent: sqlServer
  name: 'cdm'
  location: location
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  properties: {}
}

resource webApp 'Microsoft.Web/sites@2022-09-01' = {
  name: webAppName
  location: location
  kind: 'app'
  properties: {
    serverFarmId: webAppPlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'APPINSIGHTS_INSTRUMENTATIONKEY'
          value: appInsights.properties.InstrumentationKey
        }
      ]
    }
  }
  dependsOn: [
    hostingPlan
    appInsights
  ]
}

resource keyVault 'Microsoft.KeyVault/vaults@2023-02-01' = {
  name: 'cdm-kv-${uniqueString(resourceGroup().id)}'
  location: location
  properties: {
    tenantId: subscription().tenantId
    sku: {
      family: 'A'
      name: 'standard'
    }
    accessPolicies: []
    enabledForDeployment: true
    enableSoftDelete: true
  }
}

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2021-06-01' = {
  name: 'cdm-logs'
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

resource webAppPlan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: 'cdmWebAppPlan'
  location: location
  sku: {
    name: 'B1'  // Or 'F1' for free tier
    tier: 'Basic'
  }
}