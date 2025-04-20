# Azure AI Services Examples

This repository contains example code demonstrating how to use Azure AI Services in different programming languages and scenarios.

## Project Structure

```
Labfiles/
├── 01-use-azure-ai-services/      # Basic Azure AI Services usage examples
│   ├── Python/                    
│   │   ├── rest-client/          # REST API implementation
│   │   └── sdk-client/           # SDK-based implementation
│   └── C-Sharp/                  # C# implementations
│
├── 02-ai-services-security/       # Security implementation examples
│   ├── Python/
│   │   └── keyvault_client/      # Azure Key Vault integration
│   └── C-Sharp/
│
├── 03-monitor-ai-services/        # Monitoring implementation
└── 04-use-a-container/           # Containerized AI services
```

## Prerequisites

- Azure subscription
- Visual Studio Code
- Language-specific requirements:
  - For Python:
    - Python 3.8+
    - pip packages: azure-ai-textanalytics, python-dotenv, azure-identity, azure-keyvault-secrets
  - For C#:
    - .NET 7.0+
    - NuGet packages: Azure.AI.TextAnalytics, Azure.Identity, Azure.Security.KeyVault.Secrets

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/MicrosoftLearning/mslearn-ai-services
   cd mslearn-ai-services
   ```

2. Create an Azure AI Services resource in the Azure portal:
   - Search for "Azure AI services" and create a multi-service account
   - Note down the endpoint and keys from the "Keys and Endpoint" page

3. Configure your environment:
   - Copy the appropriate .env.example or appsettings.json.example file
   - Fill in your Azure AI Services endpoint and key

## Available Examples

### 1. Basic Usage (01-use-azure-ai-services)

Demonstrates basic usage of Azure AI Services using both REST API and SDK approaches:

- **REST Client**: Direct HTTP calls to the AI services endpoints
- **SDK Client**: Using the official Azure SDK for simplified integration

To run the examples:

```bash
# Python REST client
cd Labfiles/01-use-azure-ai-services/Python/rest-client
pip install -r requirements.txt
python rest-client.py

# Python SDK client
cd ../sdk-client
python sdk-client.py

# C# REST client
cd ../../C-Sharp/rest-client
dotnet run

# C# SDK client
cd ../sdk-client
dotnet run
```

### 2. Security Implementation (02-ai-services-security)

Shows how to securely handle Azure AI Services credentials using Azure Key Vault:

```bash
# Python
cd Labfiles/02-ai-services-security/Python/keyvault_client
python keyvault-client.py

# C#
cd ../../C-Sharp/keyvault_client
dotnet run
```

### 3. Monitoring (03-monitor-ai-services)

Examples of monitoring Azure AI Services usage and implementing alerts:

- REST API testing scripts for monitoring
- Alert configuration examples
- Metric visualization setup

### 4. Containerization (04-use-a-container)

Demonstrates how to run Azure AI Services in containers:

- Container deployment scripts
- Configuration examples for containerized services
- Usage examples for containerized endpoints

## Key Features

1. Language Detection
   - Supports multiple input languages
   - Available through both REST and SDK implementations
   - Includes error handling and response parsing

2. Secure Key Management
   - Azure Key Vault integration
   - Service Principal authentication
   - Secure credential handling

3. Monitoring and Alerting
   - Usage metrics tracking
   - Alert configuration
   - Diagnostic logging setup

## Error Handling

The code includes comprehensive error handling for:
- Invalid credentials
- Network issues
- Invalid input
- Service limits and throttling

## Security Notes

- Never commit .env files or credentials
- Use Key Vault for production deployments
- Rotate keys regularly
- Implement proper access controls

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

This repository is for educational purposes. For contributing to Azure AI Services, please visit the [official Azure documentation](https://docs.microsoft.com/azure/ai-services/).
