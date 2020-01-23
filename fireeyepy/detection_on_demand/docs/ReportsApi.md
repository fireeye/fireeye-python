# openapi_client.ReportsApi

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
api_instance = openapi_client.ReportsApi(openapi_client.ApiClient(configuration))
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

