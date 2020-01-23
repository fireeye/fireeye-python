# openapi_client.HashesApi

All URIs are relative to *https://feapi.marketplace.apps.fireeye.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hash_by_id**](HashesApi.md#get_hash_by_id) | **GET** /hashes/{hash_id} | Get hash analysis results


# **get_hash_by_id**
> object get_hash_by_id(hash_id)

Get hash analysis results

This endpoint fetches the results of a file submission by its MD5 hash.

### Example

* Api Key Authentication (FireEyeAPIKey):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: FireEyeAPIKey
configuration.api_key['feye-auth-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['feye-auth-key'] = 'Bearer'

# Defining host is optional and default to https://feapi.marketplace.apps.fireeye.com
configuration.host = "https://feapi.marketplace.apps.fireeye.com"
# Create an instance of the API class
api_instance = openapi_client.HashesApi(openapi_client.ApiClient(configuration))
hash_id = '4ba739fd8c216809e485e7972597c995' # str | The MD5 hash of a file you would like to request the malware analysis results for.

try:
    # Get hash analysis results
    api_response = api_instance.get_hash_by_id(hash_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HashesApi->get_hash_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_id** | **str**| The MD5 hash of a file you would like to request the malware analysis results for. | 

### Return type

**object**

### Authorization

[FireEyeAPIKey](../README.md#FireEyeAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

