"""
* @description 
* This module implements an Azure AI Services client using the official SDK.
* It demonstrates how to use the Text Analytics client for language detection
* with proper authentication and error handling.
* 
* Key features:
* - Azure AI Services SDK integration
* - Environment-based configuration
* - Interactive language detection demo
* 
* @dependencies
* - python-dotenv: Used for loading environment variables
* - azure.core.credentials: Used for Azure authentication
* - azure.ai.textanalytics: Used for Text Analytics operations
* 
* @notes
* - Requires valid Azure AI Services endpoint and key in .env file
* - Uses Text Analytics SDK for more reliable and maintainable code
* - Handles authentication automatically through SDK
"""

from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    """
    Main program entry point. Sets up the Azure AI Services client
    and runs an interactive loop for language detection.
    """
    global ai_endpoint
    global ai_key

    try:
        # Load configuration from environment
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

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
    Detects the language of provided text using Azure AI Services SDK.
    
    Args:
        text (str): The text to analyze for language detection
        
    Returns:
        str: Name of the detected language
        
    Raises:
        Exception: If the service call fails or credentials are invalid
    """
    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents = [text])[0]
    return detectedLanguage.primary_language.name

if __name__ == "__main__":
    main()