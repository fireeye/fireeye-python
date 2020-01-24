# helix.DocumentationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentation_list**](DocumentationApi.md#documentation_list) | **GET** /helix/id/hexzsq689/api/documentation/ | 


# **documentation_list**
> documentation_list()



### Example

```python
from __future__ import print_function
import time
import helix
from helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = helix.DocumentationApi()

try:
    api_instance.documentation_list()
except ApiException as e:
    print("Exception when calling DocumentationApi->documentation_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

