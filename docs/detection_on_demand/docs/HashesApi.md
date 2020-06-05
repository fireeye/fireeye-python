# fireeye.detection.HashesApi

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
import fireeye.detection
from fireeye.detection.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://feapi.marketplace.apps.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.detection.Configuration(
    host = "https://feapi.marketplace.apps.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FireEyeAPIKey
configuration = fireeye.detection.Configuration(
    host = "https://feapi.marketplace.apps.fireeye.com",
    api_key = {
        'feye-auth-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['feye-auth-key'] = 'Bearer'

# Enter a context with an instance of the API client
with fireeye.detection.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.detection.HashesApi(api_client)
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

