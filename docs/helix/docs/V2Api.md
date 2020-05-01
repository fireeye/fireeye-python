# fireeye.helix.V2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_commbrokers_short**](V2Api.md#v2_commbrokers_short) | **GET** /helix/id/hexzsq689/api/v2/commbrokers/ | 


# **v2_commbrokers_short**
> v2_commbrokers_short()



### Example

```python
from __future__ import print_function
import time
import fireeye.helix
from fireeye.helix.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fireeye.helix.V2Api()

try:
    api_instance.v2_commbrokers_short()
except ApiException as e:
    print("Exception when calling V2Api->v2_commbrokers_short: %s\n" % e)
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

