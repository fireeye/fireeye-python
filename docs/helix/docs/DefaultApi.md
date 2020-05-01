# fireeye.helix.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](DefaultApi.md#get_stats) | **GET** /helix/id/hexzsq689/api/v1/{var}incidentStats/ | View for tying together the serializer, authentication, permission and


# **get_stats**
> get_stats(var)

View for tying together the serializer, authentication, permission and

View for tying together the serializer, authentication, permission and data restrictions for accessing Incidents

### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.DefaultApi()
var = 'var_example' # str | 

try:
    # View for tying together the serializer, authentication, permission and
    api_instance.get_stats(var)
except ApiException as e:
    print("Exception when calling DefaultApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var** | **str**|  | 

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

