# SSL Certificate Verification Guide

When working with Azure AI Services, you may encounter SSL certificate verification issues, especially when making HTTPS requests to Azure endpoints. This guide provides steps to properly handle SSL verification in Python applications.

## Understanding Certifi

The `certifi` package is a carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates in Python applications. It provides:

1. A bundle of X.509 certificates of public Certificate Authorities (CAs)
2. Regular updates to maintain current security standards
3. Cross-platform compatibility for SSL certificate validation
4. Integration with popular Python HTTP libraries like `requests` and `urllib3`

### Why Certifi is Important

- Ensures secure HTTPS connections by verifying server certificates
- Maintains an up-to-date list of trusted Certificate Authorities
- Prevents man-in-the-middle attacks
- Provides consistent certificate verification across different operating systems

## Common SSL Verification Error

You might see an error like this:
```
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)
```

## Solution Steps

### 1. Install Required Dependencies

Add these packages to your `requirements.txt`:
```
certifi>=2023.7.22
requests==2.31.0
```

Then install them:
```bash
pip install -r requirements.txt
```

### 2. Update Certificate Store

Ensure you have the latest certificates:
```bash
pip install --upgrade certifi
```

### 3. Code Implementation

When making HTTPS requests, use one of these approaches:

#### Option 1: Using http.client with SSL Context
```python
import ssl
import certifi
import http.client

# Create SSL context with verified certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Use the SSL context when creating the connection
conn = http.client.HTTPSConnection(uri, context=ssl_context)
```

#### Option 2: Using requests library
```python
import requests
import certifi

response = requests.post(
    url,
    headers=headers,
    json=data,
    verify=certifi.where()
)
```

### 4. Environment Variables in Detail

Python and various SSL-related libraries use several environment variables to control certificate verification behavior:

#### Core SSL Environment Variables

1. `SSL_CERT_FILE`
   - Points to a specific SSL certificate file
   - Takes precedence over the default certificate bundle
   - Example: `export SSL_CERT_FILE=/path/to/cacert.pem`

2. `SSL_CERT_DIR`
   - Points to a directory containing multiple certificates
   - Used as a fallback if SSL_CERT_FILE is not set
   - Example: `export SSL_CERT_DIR=/etc/ssl/certs`

#### Requests Library Environment Variables

3. `REQUESTS_CA_BUNDLE`
   - Specifically used by the requests library
   - Points to a custom certificate bundle
   - Takes precedence over certifi's default bundle
   - Example: `export REQUESTS_CA_BUNDLE=/path/to/custom/cacert.pem`

4. `CURL_CA_BUNDLE`
   - Used by both curl and the requests library
   - Alternative to REQUESTS_CA_BUNDLE
   - Example: `export CURL_CA_BUNDLE=/path/to/cacert.pem`

#### Environment Variable Priority

The order of precedence for certificate verification is:
1. `SSL_CERT_FILE`
2. `REQUESTS_CA_BUNDLE`
3. `CURL_CA_BUNDLE`
4. `SSL_CERT_DIR`
5. System's default certificate store
6. certifi's built-in certificate bundle

#### When to Use Custom Certificates

Set these environment variables when:
- Working in corporate environments with internal CAs
- Dealing with self-signed certificates
- Using proxy servers with SSL inspection
- Requiring specific certificate trust chains

Example configuration in your environment:
```bash
# For Python's SSL module
export SSL_CERT_FILE=/path/to/custom/cacert.pem
export SSL_CERT_DIR=/path/to/custom/certs

# For requests library
export REQUESTS_CA_BUNDLE=/path/to/custom/cacert.pem

# For curl-based operations
export CURL_CA_BUNDLE=/path/to/cacert.pem
```

### 5. Troubleshooting

If you still experience SSL issues:

1. Verify your Python version is up to date
2. Check if your organization uses a proxy or custom certificates
3. Ensure your system time is correctly set
4. Try updating your OS's certificate store
5. Check if your firewall is blocking HTTPS connections
6. Verify environment variables are correctly set:
   ```python
   import os
   import certifi
   
   print(f"SSL_CERT_FILE: {os.environ.get('SSL_CERT_FILE')}")
   print(f"REQUESTS_CA_BUNDLE: {os.environ.get('REQUESTS_CA_BUNDLE')}")
   print(f"Certifi location: {certifi.where()}")
   ```

### 6. Best Practices

1. Always use certificate verification in production
2. Keep certifi updated regularly
3. Don't disable SSL verification (avoid `verify=False`)
4. Use environment variables for custom certificates
5. Implement proper error handling for SSL exceptions
6. Document any custom certificate configurations
7. Regular security audits of SSL/TLS configurations

### 7. For Development Only

If you're in a development environment and absolutely need to bypass SSL verification (NOT recommended for production):

```python
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

**WARNING**: Never disable SSL verification in production environments as it poses significant security risks.

## Resources

- [Python certifi documentation](https://pypi.org/project/certifi/)
- [Azure Security Best Practices](https://docs.microsoft.com/azure/security/fundamentals/best-practices-and-patterns)
- [Python SSL documentation](https://docs.python.org/3/library/ssl.html)
- [Requests Security Documentation](https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification)
- [OpenSSL Documentation](https://www.openssl.org/docs/)