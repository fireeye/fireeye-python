# fireeye.detection.ReportsApi

All URIs are relative to *https://feapi.marketplace.apps.fireeye.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report**](ReportsApi.md#get_report) | **GET** /reports/{report_id} | Get single report


# **get_report**
> OneOfReportNotExtendedReportExtended get_report(report_id, extended=extended)

Get single report

This endpoint fetches the results of a single file submission, known as a report.

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
    api_instance = fireeye.detection.ReportsApi(api_client)
    report_id = '992694b3-20ab-4245-9b4c-8f3a1b7ec3b6' # str | The report ID returned after successfully submitting a file.
extended = false # bool | Setting extended to true will allow you to see all malware engine reports. (optional)

    try:
        # Get single report
        api_response = api_instance.get_report(report_id, extended=extended)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The report ID returned after successfully submitting a file. | 
 **extended** | **bool**| Setting extended to true will allow you to see all malware engine reports. | [optional] 

### Return type

[**OneOfReportNotExtendedReportExtended**](OneOfReportNotExtendedReportExtended.md)

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

