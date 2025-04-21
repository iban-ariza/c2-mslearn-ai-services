"""
* @description 
* This module implements secure access to Azure AI Services using Azure Key Vault.
* It demonstrates best practices for storing and retrieving sensitive credentials
* using service principal authentication and Azure Key Vault integration.
* 
* Key features:
* - Azure Key Vault integration for secure key storage
* - Service Principal authentication
* - Text Analytics language detection using securely retrieved credentials
* 
* @dependencies
* - python-dotenv: Used for loading environment variables
* - azure.identity: Used for service principal authentication
* - azure.keyvault.secrets: Used for accessing Key Vault secrets
* - azure.ai.textanalytics: Used for Text Analytics operations
* 
* @notes
* - Requires service principal credentials in .env file
* - Key Vault must have appropriate access policies for the service principal
* - Uses secure credential management best practices
"""

from dotenv import load_dotenv
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential

def main():
    """
    Main program entry point. Sets up Azure Key Vault access,
    retrieves AI Services credentials, and runs language detection demo.
    """
    global ai_endpoint
    global cog_key

    try:
        # Load environment configuration
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        key_vault_name = os.getenv('KEY_VAULT')
        key_vault_secret_name = os.getenv('KEY_VAULT_SECRET_NAME')
        app_tenant = os.getenv('TENANT_ID')
        app_id = os.getenv('APP_ID')
        app_password = os.getenv('APP_PASSWORD')

        # Set up Key Vault access using service principal
        key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"
        # Authenticate using service principal credentials (https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python#defaultazurecredential)
        credential = ClientSecretCredential(app_tenant, app_id, app_password)
        keyvault_client = SecretClient(key_vault_uri, credential)
        
        # Retrieve AI Services key from Key Vault
        secret_key = keyvault_client.get_secret(key_vault_secret_name)
        cog_key = secret_key.value

        # Interactive language detection loop
        userText =''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                language = GetLanguage(userText)
                print('Language:', language)

    except Exception as ex:
        print(ex)

def GetLanguage(text):
    """
    Detects the language of provided text using Azure AI Services with
    securely retrieved credentials.
    
    Args:
        text (str): The text to analyze for language detection
        
    Returns:
        str: Name of the detected language
        
    Raises:
        Exception: If service calls fail or authentication errors occur
    """
    # Create client using endpoint and securely retrieved key
    credential = AzureKeyCredential(cog_key)
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents = [text])[0]
    return detectedLanguage.primary_language.name

if __name__ == "__main__":
    main()