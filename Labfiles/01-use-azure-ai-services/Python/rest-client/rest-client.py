"""
* @description 
* This module implements a REST client for Azure AI Services Language Detection.
* It demonstrates how to make direct HTTP requests to Azure AI Services with
* proper SSL certificate verification.
* 
* Key features:
* - Environment configuration loading
* - Direct HTTP request handling to Azure AI endpoint
* - JSON request/response processing for language detection
* - Secure SSL certificate verification
* 
* @dependencies
* - python-dotenv: Used for loading environment variables
* - http.client: Used for making HTTP requests
* - json: Used for JSON processing
* - certifi: Used for SSL certificate verification
* 
* @notes
* - Requires valid Azure AI Services endpoint and key in .env file
* - Uses Text Analytics API v3.1 for language detection
* - Handles single document language detection per request
"""

from dotenv import load_dotenv
import os
import http.client
import json
import urllib.request
import ssl
import certifi

def main():
    global ai_endpoint
    global ai_key

    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Interactive loop for language detection
        userText =''
        while userText.lower() != 'quit':
            userText = input('Enter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                GetLanguage(userText)

    except Exception as ex:
        print(ex)

def GetLanguage(text):
    """
    Detects the language of input text using Azure AI Services REST API.
    Uses proper SSL certificate verification.
    
    Args:
        text (str): Input text for language detection
        
    Returns:
        None - Prints detected language information to console
        
    Raises:
        Exception: If API call fails or response processing errors occur
    """
    try:
        # Create SSL context with verified certificates
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        
        # Construct the JSON request body
        jsonBody = {
            "documents":[
                {"id": 1,
                 "text": text}
            ]
        }

        # Display the request JSON for debugging
        print(json.dumps(jsonBody, indent=2))

        # Set up HTTP connection to the Azure AI Services endpoint with SSL verification
        uri = ai_endpoint.rstrip('/').replace('https://', '')
        conn = http.client.HTTPSConnection(uri, context=ssl_context)

        # Prepare headers with authentication key
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': ai_key
        }

        # Make the API request
        conn.request("POST", "/text/analytics/v3.1/languages?", str(jsonBody).encode('utf-8'), headers)

        # Get and process the response
        response = conn.getresponse()
        data = response.read().decode("UTF-8")

        # Handle successful response
        if response.status == 200:
            results = json.loads(data)
            print(json.dumps(results, indent=2))

            # Extract and display detected language
            for document in results["documents"]:
                print("\nLanguage:", document["detectedLanguage"]["name"])
        else:
            # Handle API errors
            print(data)

        conn.close()

    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    main()